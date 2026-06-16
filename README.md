# AI Travel Planning System using LangGraph

A production-style **multi-agent travel planning application** built with **LangGraph**. Four specialized AI agents collaborate to search flights, find hotels, build itineraries, and deliver a complete trip plan — with persistent conversation memory backed by PostgreSQL.

---

## Application Preview

![AI Travel Booking System — homepage with hero banner, destination cards, and trip preferences](docs/screenshots/Hero_Page.jpeg)

The Streamlit dashboard opens with a cinematic full-width hero — an airplane above golden clouds — with the **AI Travel Booking System** title centered on the image. The left sidebar shows your session ID, the tech stack (LangGraph, Groq, PostgreSQL, Tavily, AviationStack), and the four-agent pipeline at a glance.

Below the hero, five destination cards (Tokyo, Paris, Bangkok, Rome, Dubai) invite quick exploration. The main panel lets you describe your trip in natural language or tap preset prompts like *“7-day Japan under ₹2L”*. Sliders set **duration** and **budget**, while dropdowns and toggles capture travel style, domestic vs international scope, and preferred region — so every request sent to the agents is rich, structured, and personal.

---

## Features

### Multi-Agent Pipeline
| Agent | Responsibility |
|-------|----------------|
| **Flight Agent** | Searches flights via AviationStack API |
| **Hotel Agent** | Retrieves hotel and destination data via Tavily |
| **Itinerary Agent** | Generates a day-wise travel itinerary using Groq LLM |
| **Final Agent** | Combines all results into a polished travel plan |

### Web Interface (Streamlit)
- Full-width hero header with centered branding
- Quick destination cards and one-click trip presets
- **Trip preferences:** duration, budget, travel style
- **Domestic (Inter-state) / International** trip scope
- **Travel modes:** Air, Road, Train, Bus, Water / Ferry
- **Adventure options:** Camping, Trekking, Safari, and more
- Live agent pipeline with progress tracking
- Tabbed trip breakdown (Flights · Hotels · Itinerary · Final Plan)
- Markdown export and auto-save to `travel_plans/`
- Session-based recent plan history

### Backend & Memory
- LangGraph state machine with PostgreSQL checkpointing
- Per-user thread memory via `thread_id`
- Streaming agent updates for real-time UI feedback

---

## Architecture

```
User Input (Streamlit / CLI)
        │
        ▼
┌───────────────────────────────────────────┐
│           LangGraph StateGraph            │
│                                           │
│  Flight Agent → Hotel Agent → Itinerary   │
│       Agent → Final Agent                 │
└───────────────────────────────────────────┘
        │                    │
        ▼                    ▼
  External APIs         PostgreSQL
  (Groq, Tavily,        (conversation
   AviationStack)        memory)
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Orchestration | LangGraph, LangChain |
| LLM | Groq — Llama 3.3 70B |
| Memory | PostgreSQL + `langgraph-checkpoint-postgres` |
| Flight data | AviationStack API |
| Web search | Tavily API |
| Frontend | Streamlit |
| Runtime | Python 3.11+ |

---

## Project Structure

```
AI-Travel-Planning-System-using-LangGraph/
├── main.py                 # LangGraph graph, agents, PostgreSQL checkpointer
├── frontend.py             # Streamlit web application
├── tools/
│   ├── flight_tool.py      # AviationStack flight search
│   └── tavily_tool.py      # Tavily web search for hotels
├── travel_plans/           # Auto-saved markdown plans (generated at runtime)
├── docs/screenshots/       # Application screenshots for README
├── .env                    # API keys and database URL (not committed)
└── README.md
```

---

## Prerequisites

- Python 3.11 or later
- PostgreSQL 14+ (local install or Docker)
- API keys for [Groq](https://console.groq.com), [Tavily](https://tavily.com), and [AviationStack](https://aviationstack.com)

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd AI-Travel-Planning-System-using-LangGraph
```

### 2. Create and activate a virtual environment

**Windows (PowerShell)**

```powershell
python -m venv langgraph_env3
.\langgraph_env3\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python -m venv langgraph_env3
source langgraph_env3/bin/activate
```

### 3. Install dependencies

```bash
pip install langgraph langchain langchain-groq langchain-community psycopg[binary] python-dotenv tavily-python requests streamlit
pip install -U "psycopg[binary,pool]" langgraph-checkpoint-postgres
```

### 4. Set up PostgreSQL

Create a database for LangGraph memory:

```sql
CREATE DATABASE langgraph_memory;
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/langgraph_memory
```

> Use `KEY=value` format with no spaces around `=`.

---

## Usage

### CLI (terminal)

```bash
python main.py
```

Example prompt:

```
Plan a complete 7-day Japan trip including flights, hotels and sightseeing under ₹2 lakhs.
```

### Web application (Streamlit)

Always run Streamlit from the project virtual environment:

**Windows**

```powershell
.\langgraph_env3\Scripts\python.exe -m streamlit run frontend.py
```

**macOS / Linux**

```bash
python -m streamlit run frontend.py
```

Open the URL shown in the terminal (default: `http://localhost:8501`).

---

## Agent Workflow

1. **Flight Agent** — parses the user query and fetches flight options
2. **Hotel Agent** — searches hotels and accommodation via Tavily
3. **Itinerary Agent** — builds a structured day-wise itinerary
4. **Final Agent** — synthesizes flights, hotels, and itinerary into one response
5. **PostgreSQL** — persists graph state and conversation history per `thread_id`

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `No module named streamlit` / `psycopg` | Activate `langgraph_env3` or use the venv Python path explicitly |
| `CREATE INDEX CONCURRENTLY cannot run inside a transaction block` | Ensure `main.py` uses `psycopg.connect(DATABASE_URL, autocommit=True)` |
| `InvalidAPIKeyError` (Tavily) | Verify `TAVILY_API_KEY` in `.env` is valid and complete |
| Database connection failed | Check PostgreSQL is running, credentials, port, and database name in `DATABASE_URL` |

---

## Example `.env` Reference

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxx
AVIATIONSTACK_API_KEY=xxxxxxxxxxxxxxxx
DATABASE_URL=postgresql://postgres:12345@localhost:5432/langgraph_memory
```

---



## Acknowledgements

Built with [LangGraph](https://github.com/langchain-ai/langgraph), [Groq](https://groq.com), [Streamlit](https://streamlit.io), and open travel data APIs.
