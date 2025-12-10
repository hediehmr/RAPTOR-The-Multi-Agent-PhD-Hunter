import json
import uuid
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools.function_tool import FunctionTool

# Import your custom database
from database import PositionDatabase

# --- STATE MANAGEMENT ---
@dataclass
class UserMemory:
    resume_text: Optional[str] = None
    constraints: Dict[str, Any] = field(default_factory=lambda: {
        "budget": 0, 
        "nationality": "Unknown"
    })

# Global instances (Note: In production, use a proper database or session manager)
user_state = UserMemory()
email_approval_state = {} 

# --- TOOLS ---
def fetch_positions_tool() -> str:
    """Fetches the list of open academic positions."""
    db = PositionDatabase(source_type="mock")
    positions = db.load_positions()
    print(f"✅ Database Loaded: {len(positions)} positions.")
    return json.dumps(positions)

def profile_loader_tool(resume_text: Optional[str] = None, budget: Optional[int] = None, nationality: Optional[str] = None) -> str:
    """Saves user profile data into memory."""
    global user_state
    if resume_text:
        user_state.resume_text = resume_text
        print(f"DEBUG: Resume saved (Length: {len(resume_text)})")
    if budget is not None:
        user_state.constraints["budget"] = budget
    if nationality:
        user_state.constraints["nationality"] = nationality

    if user_state.resume_text:
        return "PROCEED: Profile is ready."
    return "STOP: Resume Missing."

def safe_email_tool(email_content: str, destination: str, position_id: int) -> str:
    """Checks if sending email is approved."""
    if email_approval_state.get(position_id):
        print(f"📧 [SENT] Email to {destination}")
        return f"SUCCESS: Email sent to {destination}."
    return f"STOP: APPROVAL_NEEDED for Position {position_id}."

# --- AGENT DEFINITIONS ---
initializer_agent = LlmAgent(
    name="Initializer",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="""
    You are the Profile Manager Agent.
    PROTOCOL:
    1. ALWAYS call 'profile_loader_tool' immediately with info provided.
    2. IF "STOP": Ask for resume.
    3. IF "PROCEED": Respond EXACTLY "INITIALIZATION_COMPLETE".
    """,
    tools=[FunctionTool(profile_loader_tool)]
)

analyst_agent = LlmAgent(
    name="Analyst",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="""
    You are the Job Analyst.
    PROTOCOL:
    1. Call 'fetch_positions_tool'.
    2. Filter jobs based on User Context. Reject if cost > budget.
    3. Output the top valid matches as a JSON list. JUST the JSON.
    """,
    tools=[FunctionTool(fetch_positions_tool)]
)

writer_agent = LlmAgent(
    name="Writer",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="""
    You are an Academic Writer.
    Generate a professional email for the Job provided.
    Use the Resume Context provided to personalize it.
    """,
    tools=[] 
)

executor_agent = LlmAgent(
    name="Executor",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="""
    You are the Email Sender Agent.
    PROTOCOL:
    1. ALWAYS call 'safe_email_tool' first.
    2. IF "STOP: APPROVAL_NEEDED": Inform user waiting for approval.
    3. IF user says "Approved": Call 'safe_email_tool' AGAIN.
    4. IF "SUCCESS": Confirm email sent.
    """,
    tools=[FunctionTool(safe_email_tool)]
)