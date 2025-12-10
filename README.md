# 🦖 RAPTOR: The Multi-Agent PhD Hunter

**An autonomous, stateful agentic workflow for academic applications.**

RAPTOR (Recruiting Agent for PhD Target Optimization & Research) is a multi-agent system designed to automate the search, filtering, and application process for academic positions. Unlike simple scripts, it features **human-in-the-loop (HITL) guardrails**, **stateful session management**, and **persisted memory**.

## 🏗 Architecture
The system follows a **Hub-and-Spoke** architecture orchestrated by `main.py`:

1.  **Initializer Agent**: Ingests user profile (Resume, GPA, Budget) and initializes the session state.
2.  **Analyst Agent**: Queries the `PositionDatabase` (Mock/Production) and filters roles based on hard constraints (Budget < Cost).
3.  **Writer Agent**: Uses RAG-like context to draft hyper-personalized cold emails to professors.
4.  **Executor Agent**: Handles the final mile delivery with a **Human-in-the-Loop** approval stop.

## 🚀 Usage

### Prerequisites
- Python 3.10+
- Google GenAI SDK

### Installation
```bash
git clone [https://github.com/hediehmr/RAPTOR-The-Multi-Agent-PhD-Hunter.git](https://github.com/hediehmr/RAPTOR-The-Multi-Agent-PhD-Hunter.git)
cd RAPTOR-The-Multi-Agent-PhD-Hunter
pip install -r requirements.txt
