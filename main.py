import asyncio
import uuid
import json
from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.adk.apps.app import App, ResumabilityConfig
from google.adk.runners import Runner

# Import from our new modules
from agents import (
    initializer_agent, analyst_agent, writer_agent, executor_agent,
    user_state, email_approval_state # Importing state to read it for prompts
)

async def main():
    # --- SETUP RUNNERS ---
    session_service = InMemorySessionService()

    init_runner = Runner(
        app=App(name="InitializerApp", root_agent=initializer_agent, resumability_config=ResumabilityConfig(is_resumable=True)),
        session_service=session_service
    )
    analyst_runner = Runner(
        app=App(name="AnalystApp", root_agent=analyst_agent),
        session_service=session_service
    )
    writer_runner = Runner(
        app=App(name="WriterApp", root_agent=writer_agent),
        session_service=session_service
    )
    executor_runner = Runner(
        app=App(name="ExecutorApp", root_agent=executor_agent, resumability_config=ResumabilityConfig(is_resumable=True)),
        session_service=session_service
    )

    # --- EXECUTION ---
    session_id = f"sess_{uuid.uuid4().hex[:6]}"
    user_id = "Hedieh"
    print(f"PIPELINE STARTED – Session: {session_id}\n")

    # 1. INITIALIZATION
    await session_service.create_session(user_id=user_id, session_id=session_id, app_name="InitializerApp")
    
    user_input = """Hi, I want to apply for PhD positions.My resume:
        Hedieh Moftakhari – hedieh.rm@gmail.com
        M.Sc. GPA 3.95/4.0 – GRE 329 – TOEFL 108
        Skills: Python, C++, CUDA, PyTorch, model quantization, efficient ML
        Nationality: Iranian – Max fee budget: 120 USD"""

    step1_done = False
    msg = types.Content(role="user", parts=[types.Part(text=user_input)])
    
    async for event in init_runner.run_async(new_message=msg, user_id=user_id, session_id=session_id):
        if event.content and event.content.parts:
            resp = event.content.parts[0].text
            print(f"Agent: {resp}")
            if "INITIALIZATION_COMPLETE" in resp:
                step1_done = True

    if not step1_done: return

    # 2. ANALYSIS
    analyst_session_id = f"analyst_{uuid.uuid4().hex[:6]}"
    print(f"\n--- 🕵️‍♂️ Step 2: Analyst ---")
    await session_service.create_session(app_name="AnalystApp", user_id=user_id, session_id=analyst_session_id)
    
    analyst_prompt = f"Find jobs for this profile: {user_state.resume_text} Constraints: {user_state.constraints}"
    analyst_msg = types.Content(role="user", parts=[types.Part(text=analyst_prompt)])
    
    found_positions_json = ""
    async for event in analyst_runner.run_async(new_message=analyst_msg, user_id=user_id, session_id=analyst_session_id):
         if event.content and event.content.parts:
            resp = event.content.parts[0].text
            print(f"Analyst: {resp}")
            found_positions_json = resp

    if not found_positions_json: return

    # 3. DRAFTING
    print("\n--- ✍️ Step 3: Drafter ---")
    positions_list = json.loads(found_positions_json)
    target_position = positions_list[0]
    
    writer_prompt = f"""
    Write a cold email for: {target_position.get('title')} at {target_position.get('university', {}).get('name')}
    User Stats: {user_state.resume_text[:100]}...
    """
    
    writer_msg = types.Content(role="user", parts=[types.Part(text=writer_prompt)])
    email_draft_content = ""
    writer_session_id = f"writer_{uuid.uuid4().hex[:6]}"
    
    await session_service.create_session(app_name="WriterApp", user_id=user_id, session_id=writer_session_id)
    async for event in writer_runner.run_async(new_message=writer_msg, user_id=user_id, session_id=writer_session_id):
        if event.content and event.content.parts:
            resp = event.content.parts[0].text
            print(f"Writer: {resp[:100]}... (truncated)")
            email_draft_content = resp

    # 4. EXECUTION (With HITL Loop)
    if email_draft_content:
        print("\n--- 📧 Step 4: Executor ---")
        exec_session_id = f"exec_{uuid.uuid4().hex[:6]}"
        await session_service.create_session(app_name="ExecutorApp", user_id=user_id, session_id=exec_session_id)

        target_email = target_position.get("professor", {}).get("email", "unknown@univ.edu")
        target_id = target_position.get("id", 0)
        executor_prompt = f"Send this email to {target_email} (Position ID: {target_id}). Content: {email_draft_content[:50]}..."
        
        exec_msg = types.Content(role="user", parts=[types.Part(text=executor_prompt)])
        saved_event_id = None

        async for event in executor_runner.run_async(new_message=exec_msg, user_id=user_id, session_id=exec_session_id):
            if event.content and event.content.parts:
                resp = event.content.parts[0].text
                print(f"Agent: {resp}")
                saved_event_id = event.invocation_id

        # Simulating Human Approval
        if saved_event_id:
            print(f"\n⏸️ SYSTEM PAUSED: Approval needed for {target_email}")
            email_approval_state[target_id] = True
            print("✅ State Updated: Approved.")
            
            resume_msg = types.Content(role="user", parts=[types.Part(text="Approved.")])
            async for resume_event in executor_runner.run_async(new_message=resume_msg, user_id=user_id, session_id=exec_session_id, invocation_id=saved_event_id):
                if resume_event.content and resume_event.content.parts:
                    print(f"Agent (Resumed): {resume_event.content.parts[0].text}")

    print("\n🦅 PIPELINE FINISHED SUCCESSFULLY.")

if __name__ == "__main__":
    asyncio.run(main())