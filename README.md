🦖 RAPTOR: The Multi-Agent PhD Hunter

Problem Statement
Applying for academic positions (PhD/Master's) is a high-friction process. Candidates often waste hours filtering through irrelevant listings that don't match their hard constraints (e.g., application budget, visa/nationality restrictions) or soft constraints (research interests). Furthermore, customizing emails for every single professor is mentally exhausting and prone to errors.
The Solution: RAPTOR
RAPTOR (Research Application & Parsing Orchestrator) is a multi-agent system designed to act as a personalized academic concierge. Unlike simple scrapers, RAPTOR understands the candidate's full profile (resume text) and constraints. It doesn't just "search"; it filters, reasons, drafts, and executes, but only with strict human approval at critical junctures.
System Architecture & Design
I chose a Python-orchestrated multi-agent Pipeline instead of a single monolithic agent. This ensures reliability and strictly controlled state transitions. The system consists of four specialized agents:
Agent 1: The Initializer (Gatekeeper): Ensures the system never starts without a loaded user profile. It uses a "Guardrail Pattern" to halt execution until the resume and constraints (budget, nationality) are stored in the shared state.
Agent 2: The Analyst (Reasoning Engine): Acts as the brain. It fetches raw position data and applies RAG-style filtering. It intelligently rejects positions that violate hard constraints (e.g., "Application cost > User Budget") and ranks the rest based on resume similarity.
Agent 3: The Drafter (Content Gen): Uses the Gemini 2.5 Flash model to generate hyper-personalized outreach emails, mapping specific resume skills to the professor's research area.
Agent 4: The Executor (Final Guardrail): Handles the sensitive action of sending emails. It implements a Human-in-the-Loop (HITL) flow, pausing execution and presenting the draft to the user. It only calls the send_email_tool upon receiving an explicit "APPROVE" or "SEND" command.
Key Features Implemented (Course Concepts)
This project demonstrates three core pillars of Agentic AI:
State Management (Shared Memory): I implemented a custom ApplicationState class that acts as the "Single Source of Truth," preserving the user's resume and selected jobs across the entire lifecycle of the application.
Tool Use & Custom Functions: The agents utilize custom tools (profile_loader, fetch_positions, send_email) to interact with the external world and update the internal state.
Human-in-the-Loop (Resumability Logic): The system is designed to be asynchronous and interactive. It does not run blindly; it negotiates with the user during Initialization and Execution, ensuring the user is always in control of the final output.
How it Works (Demo Flow)
User: "Hi, I want to apply." -> System: "Please provide a resume." (Gatekeeper active)
User: Provides resume & budget. -> System: Saves to memory, transitions to Analysis.
System: Filters 100+ positions, identifies the top matching positions, and drafts personalized emails.
System: "Draft ready. Send?" -> User: "Wait" or "Send". (Executor active)
