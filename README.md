# ✈️ Travexa AI — End-to-End Multi-Agent AI Travel Planner

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LangChain-Framework-1C3C3C?logo=langchain&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/LangGraph-Multi--Agent_Workflow-1C3C3C" alt="LangGraph">
  <img src="https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/Tavily-Search-FF6B35" alt="Tavily">
  <img src="https://img.shields.io/badge/AviationStack-Flight_API-2563EB" alt="AviationStack">
  <img src="https://img.shields.io/badge/FastAPI-Web_App-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-Persistence-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/AI-Multi--Agent_AI-blueviolet" alt="Multi-Agent AI">
  <img src="https://img.shields.io/badge/UI-Purple_Neon-A855F7" alt="Purple Neon UI">
  <img src="https://img.shields.io/badge/Git-Version_Control-F05032?logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white" alt="GitHub">
</p>

<p align="center">
  <strong>
    An end-to-end multi-agent AI travel planning application that searches flights,
    researches hotels, creates personalized itineraries, and generates structured
    travel plans through a LangGraph-powered workflow.
  </strong>
</p>

<p align="center">
  🧳 <strong>User Travel Request</strong> →
  ✈️ <strong>Flight Agent</strong> →
  🏨 <strong>Hotel Agent</strong> →
  🗺️ <strong>Itinerary Agent</strong> →
  🤖 <strong>Final Response Agent</strong>
</p>

<p align="center">
  <a href="#user-interface">Screenshots</a> ·
  <a href="#installation">Installation</a>
</p>

---

## 📌 Overview

**Travexa AI** is an end-to-end multi-agent AI travel planning application built using **Python, LangGraph, LangChain, OpenAI, Tavily, AviationStack, FastAPI, PostgreSQL, HTML, CSS, and JavaScript**.

Users provide a natural-language travel request such as:

> Plan a complete 7-day England trip from Sri Lanka including flights, hotels, sightseeing, and a budget under 3 lakhs.

Travexa AI processes the request through a specialized sequential workflow:

1. **Flight Agent** retrieves relevant flight information.
2. **Hotel Agent** searches for accommodation information.
3. **Itinerary Agent** combines the user's request with flight and hotel information to build a practical itinerary.
4. **Final Response Agent** creates a structured travel plan containing flights, hotels, daily activities, budget guidance, and recommendations.

The application uses a **LangGraph `StateGraph`** to coordinate the travel-planning workflow.

A PostgreSQL-backed **LangGraph `PostgresSaver`** maintains graph checkpoints using conversation-specific `thread_id` values.

A custom **purple neon HTML, CSS, and JavaScript interface** provides a modern AI travel-planning experience with 3D-style visual elements, animated status indicators, quick prompts, Markdown-rendered results, copy controls, and PDF export.

---

## ✨ Features

- ✈️ AI-powered travel planning.
- 🤖 Multi-agent workflow built with LangGraph.
- 🧭 Sequential specialized-agent execution.
- ✈️ Flight information using AviationStack.
- 🏨 Hotel research using Tavily.
- 🔎 External web information retrieval.
- 🗺️ AI-generated personalized itineraries.
- 📅 Day-by-day travel planning.
- 💰 Budget-aware itinerary generation.
- 🤖 OpenAI-powered itinerary generation.
- ✨ AI-generated final travel responses.
- 💾 PostgreSQL-backed LangGraph checkpoints.
- 🧵 Conversation-specific thread identifiers.
- 🌐 FastAPI web application.
- 📡 REST API for travel-plan generation.
- ❤️ Application health-check endpoint.
- 🎨 Custom purple neon interface.
- 🌐 3D-style animated AI travel globe.
- ✈️ Animated travel-themed elements.
- ⏳ Travel-planning activity indicators.
- ⚡ Quick travel prompts.
- 📝 Markdown-rendered AI responses.
- 📋 Copy generated travel plans.
- 📄 Export travel plans as PDF.
- 📱 Responsive interface.
- 🔐 Environment-variable configuration.
- 🧩 Modular backend, tools, frontend, and API structure.

---

<a id="user-interface"></a>

## 📸 User Interface

### Travexa AI Home

The Travexa AI home interface provides a modern purple-neon travel planning experience with an animated AI travel globe, travel-focused visual elements, quick prompts, and the main planning workspace.

<p align="center">
  <img src="assets/screenshots/home.png" alt="Travexa AI home interface" width="1000">
</p>

### AI Travel Request

Users can describe their complete trip requirements using natural language, including destination, duration, budget, flights, hotels, and sightseeing preferences.

<p align="center">
  <img src="assets/screenshots/travel-request.png" alt="Travexa AI travel request interface" width="1000">
</p>

### AI Travel Plan

Travexa AI processes the request through the LangGraph workflow and presents the generated travel plan inside the result workspace.

<p align="center">
  <img src="assets/screenshots/travel-result.png" alt="Travexa AI generated travel plan" width="1000">
</p>

### Flight Information

The Flight Agent retrieves available flight information using the AviationStack-powered flight search tool.

<p align="center">
  <img src="assets/screenshots/flight-result.png" alt="Travexa AI flight information results" width="1000">
</p>

### Day-by-Day Itinerary

The Itinerary Agent combines the user's travel request with flight and hotel information to create a practical day-by-day travel itinerary.

<p align="center">
  <img src="assets/screenshots/itinerary.png" alt="Travexa AI generated day-by-day itinerary" width="1000">
</p>

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    USER["🧳 User Travel Request"] --> UI["🎨 Travexa AI Web Interface"]

    UI --> API["🌐 FastAPI Application"]

    API --> GRAPH["🦜 LangGraph Travel Workflow"]

    GRAPH --> FLIGHT["✈️ Flight Agent"]
    FLIGHT --> AVIATION["🌍 AviationStack API"]

    FLIGHT --> HOTEL["🏨 Hotel Agent"]
    HOTEL --> TAVILY["🔎 Tavily Search"]

    HOTEL --> ITINERARY["🗺️ Itinerary Agent"]
    ITINERARY --> OPENAI1["🤖 OpenAI"]

    ITINERARY --> FINAL["✨ Final Response Agent"]
    FINAL --> OPENAI2["🤖 OpenAI"]

    FINAL --> RESULT["📋 Personalized Travel Plan"]

    GRAPH -. Checkpoints .-> POSTGRES["🐘 PostgreSQL"]

    RESULT --> API
    API --> UI
```

The current Travexa AI workflow is sequential:

```text
START
  ↓
✈️ Flight Agent
  ↓
🏨 Hotel Agent
  ↓
🗺️ Itinerary Agent
  ↓
🤖 Final Response Agent
  ↓
END
```

Each stage enriches the shared `TravelState` before passing it to the next stage.

---

## 🔄 How It Works

### 1️⃣ User Enters a Travel Request

The user enters a natural-language travel request through the Travexa AI web interface.

Example:

> Plan a complete 7-day England trip from Sri Lanka including flights, hotels and sightseeing under 3 lakhs.

The frontend sends the request to:

```text
POST /api/travel
```

Request structure:

```json
{
  "message": "Plan a 7-day England trip from Sri Lanka under 3 lakhs.",
  "thread_id": null
}
```

---

### 2️⃣ FastAPI Validates the Request

FastAPI receives the request through the `TravelRequest` Pydantic model:

```python
class TravelRequest(BaseModel):
    message: str
    thread_id: str | None = None
```

The message is stripped and validated before entering the travel workflow.

Empty messages return an HTTP `400` response.

Valid requests are passed to:

```python
run_travel_agent(
    user_input=user_message,
    thread_id=request_data.thread_id
)
```

---

### 3️⃣ Conversation Thread Is Prepared

If the request does not contain a `thread_id`, Travexa AI creates one:

```python
if not thread_id:
    thread_id = f"user_{uuid.uuid4().hex}"
```

The identifier is passed to LangGraph:

```python
config = {
    "configurable": {
        "thread_id": thread_id
    }
}
```

This allows graph checkpoints to remain associated with the corresponding conversation thread.

---

### 4️⃣ Flight Agent Searches for Flights

The first graph node is:

```python
flight_agent
```

It receives the original user query and calls:

```python
search_flights(query)
```

The dedicated flight tool retrieves flight information using AviationStack.

The result is stored in:

```python
flight_results
```

The updated state is then passed to the Hotel Agent.

---

### 5️⃣ Hotel Agent Researches Accommodation

The Hotel Agent creates a hotel-search query:

```python
query = f"Best Hotels for {state['user_query']}"
```

It calls:

```python
tavily_search(query)
```

The returned accommodation information is stored in:

```python
hotel_results
```

The state then continues to the Itinerary Agent.

---

### 6️⃣ Itinerary Agent Creates the Travel Plan

The Itinerary Agent receives:

- Original travel request.
- Flight results.
- Hotel results.

The agent constructs a prompt containing the accumulated travel information.

The model is instructed to behave as an expert travel planner:

```python
response = llm.invoke([
    SystemMessage(
        content="You are an expert travel planner."
    ),
    HumanMessage(content=prompt)
])
```

The generated itinerary is stored in:

```python
itinerary
```

---

### 7️⃣ Final Response Agent Creates the Final Answer

The Final Response Agent receives:

```text
User Request
+
Flight Results
+
Hotel Results
+
Generated Itinerary
```

It produces a structured response containing:

```text
1. Trip Summary
2. Flight Information
3. Hotel Suggestions
4. Day-by-Day Itinerary
5. Estimated Budget
6. Final Recommendations
```

The final prompt also tells the model to mention when live flight information does not contain ticket pricing.

---

### 8️⃣ FastAPI Returns the Result

The API returns structured JSON:

```json
{
  "success": true,
  "thread_id": "user_example",
  "answer": "Generated final travel plan...",
  "flight_results": "Flight information...",
  "hotel_results": "Hotel information...",
  "itinerary": "Generated itinerary...",
  "llm_calls": 4
}
```

The browser renders the final `answer` inside the Travexa AI result workspace.

---

## 🧠 Agents and Responsibilities

| Component | Type | Responsibility |
| --- | --- | --- |
| ✈️ Flight Agent | Travel-data node | Retrieve relevant flight information |
| 🏨 Hotel Agent | Research node | Search for accommodation information |
| 🗺️ Itinerary Agent | LLM node | Build a practical, budget-aware itinerary |
| 🤖 Final Response Agent | LLM node | Produce the final structured travel plan |
| ✈️ `search_flights` | External API tool | Retrieve flight information through AviationStack |
| 🔎 `tavily_search` | Search tool | Retrieve hotel and travel information |
| 🐘 `PostgresSaver` | Checkpoint store | Persist LangGraph checkpoints by thread |

The current implementation uses four specialized sequential graph nodes.

---

## 🧠 Shared Travel State

Travexa AI uses a typed state shared across the LangGraph workflow:

```python
class TravelState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    user_query: str
    flight_results: str
    hotel_results: str
    itinerary: str
    llm_calls: int
```

| State Field | Purpose |
| --- | --- |
| `messages` | Maintain messages produced during graph execution |
| `user_query` | Store the original travel request |
| `flight_results` | Store flight-search information |
| `hotel_results` | Store hotel-search information |
| `itinerary` | Store the generated travel itinerary |
| `llm_calls` | Maintain the workflow's current processing counter |

Each graph node returns updated values that become part of the shared state.

---

## 🦜 LangGraph Workflow Composition

The travel workflow is constructed using `StateGraph`:

```python
graph = StateGraph(TravelState)

graph.add_node("flight_agent", flight_agent)
graph.add_node("hotel_agent", hotel_agent)
graph.add_node("itinerary_agent", itinerary_agent)
graph.add_node("final_agent", final_agent)

graph.add_edge(START, "flight_agent")
graph.add_edge("flight_agent", "hotel_agent")
graph.add_edge("hotel_agent", "itinerary_agent")
graph.add_edge("itinerary_agent", "final_agent")
graph.add_edge("final_agent", END)
```

The graph is compiled with PostgreSQL checkpoint persistence:

```python
travel_graph = graph.compile(
    checkpointer=checkpointer
)
```

This keeps each stage of travel planning separated while allowing information to flow through one shared state.

---

## 🌐 Travel Tools

### ✈️ AviationStack Flight Search

Travexa AI imports its flight-search implementation from:

```python
from tools.flight_tool import search_flights
```

The Flight Agent calls:

```python
flight_data = search_flights(query)
```

The flight tool processes travel-location information and retrieves available flight information through AviationStack.

The flight-search implementation also supports location-to-airport resolution for travel queries.

Flight API results may not always contain live ticket prices.

---

### 🔎 Tavily Hotel Research

Hotel information is retrieved through:

```python
from tools.tavily_tool import tavily_search
```

The Hotel Agent builds a search query:

```python
query = f"Best Hotels for {state['user_query']}"
```

and calls:

```python
hotel_results = tavily_search(query)
```

The search results become part of the context supplied to the Itinerary Agent and Final Response Agent.

---

### 🤖 OpenAI Travel Planning

The Itinerary Agent and Final Response Agent use a `ChatOpenAI` instance through `langchain-openai`.

Conceptually:

```python
llm = ChatOpenAI(
    model=YOUR_SUPPORTED_MODEL,
    api_key=OPENAI_API_KEY
)
```

The exact model configured in `backend.py` must be available to the OpenAI API account being used.

---

## 💾 PostgreSQL Persistence

Travexa AI uses PostgreSQL as the backing store for LangGraph checkpoints.

The connection URL is loaded from the environment:

```python
database_url = os.getenv("DATABASE_URL")
```

When `sslmode` is not already present, the application adds:

```text
sslmode=require
```

The PostgreSQL connection is created using Psycopg:

```python
_conn = psycopg.connect(
    DATABASE_URL,
    autocommit=True,
    row_factory=dict_row
)
```

LangGraph persistence is configured using:

```python
checkpointer = PostgresSaver(_conn)

checkpointer.setup()
```

The checkpointer is attached when the graph is compiled:

```python
travel_graph = graph.compile(
    checkpointer=checkpointer
)
```

Each graph invocation receives:

```python
config = {
    "configurable": {
        "thread_id": thread_id
    }
}
```

This associates LangGraph checkpoints with the selected travel-planning thread.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| --- | --- |
| 🐍 Python | Core application language |
| 🦜 LangChain | Model integration and message handling |
| 🔀 LangGraph | Multi-agent travel workflow |
| 🤖 OpenAI | Itinerary and final-response generation |
| 🔗 langchain-openai | LangChain integration with OpenAI |
| ✈️ AviationStack | Flight-information API |
| 🔎 Tavily | Hotel and travel research |
| 🌐 FastAPI | Backend API and web application |
| ⚡ Uvicorn | ASGI application server |
| 📄 Jinja2 | Frontend template rendering |
| 🐘 PostgreSQL | LangGraph checkpoint persistence |
| 🔗 Psycopg | PostgreSQL Python driver |
| 🔐 python-dotenv | Environment-variable loading |
| 🔒 certifi | Certificate configuration |
| 🌍 airportsdata | Airport metadata |
| 🌎 pycountry | Country information |
| 🎨 HTML + CSS | Interface structure, styling, and animation |
| ⚙️ JavaScript | API requests and frontend interactions |
| 📝 Marked | Markdown response rendering |
| 📄 html2pdf.js | Travel-plan PDF export |
| 🧰 Git | Version control |
| 🐙 GitHub | Source-code hosting |

---

## 📦 Main Python Libraries

```text
fastapi
uvicorn
jinja2
pydantic
python-dotenv
langchain
langchain-core
langchain-openai
langgraph
langgraph-checkpoint-postgres
psycopg
requests
certifi
airportsdata
pycountry
tavily-python
```

Install the exact project dependencies using `requirements.txt`.

---

## 📁 Project Structure

```text
Travexa-AI-Multi-Agent-Travel-Planner/
│
├── assets/
│   └── screenshots/
│       ├── home.png
│       ├── travel-request.png
│       ├── travel-result.png
│       ├── flight-result.png
│       └── itinerary.png
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── tools/
│   ├── __init__.py
│   ├── flight_tool.py
│   └── tavily_tool.py
│
├── app.py
├── backend.py
├── README.md
├── requirements.txt
├── test.py
├── .gitignore
└── .env
```

| Path | Purpose |
| --- | --- |
| `app.py` | FastAPI application, frontend route, travel API, and health endpoint |
| `backend.py` | LangGraph agents, workflow, OpenAI integration, and PostgreSQL persistence |
| `tools/flight_tool.py` | Flight-search and location-resolution implementation |
| `tools/tavily_tool.py` | Tavily-based travel and hotel search |
| `templates/index.html` | Travexa AI frontend markup |
| `static/style.css` | Purple-neon interface and animations |
| `static/script.js` | Frontend interaction and API requests |
| `assets/screenshots/` | README interface screenshots |
| `requirements.txt` | Python dependencies |
| `test.py` | Project testing/development file |
| `.gitignore` | Files excluded from version control |
| `.env` | Local API credentials and configuration |

The `.env` file and `travexa-env/` virtual environment should remain excluded from Git.

---

<a id="installation"></a>

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sudeeraattanayake/Travexa-AI-Multi-Agent-Travel-Planner.git
cd Travexa-AI-Multi-Agent-Travel-Planner
```

### 2️⃣ Create a Python 3.11 Virtual Environment

#### Windows PowerShell

```powershell
py -3.11 -m venv travexa-env
.\travexa-env\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3.11 -m venv travexa-env
source travexa-env/bin/activate
```

### 3️⃣ Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

Create a `.env` file beside `app.py`:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here

TAVILY_API_KEY=your_tavily_api_key_here

AVIATIONSTACK_API_KEY=your_aviationstack_api_key_here
AVIATIONSTACK_BASE_URL=https://api.aviationstack.com/v1

DATABASE_URL=your_postgresql_connection_url_here

DEFAULT_ORIGIN_IATA=CMB
```

Do not commit real API keys or database credentials.

### 6️⃣ Run Travexa AI

```bash
python app.py
```

Open:

```text
http://127.0.0.1:8000
```

FastAPI interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

ReDoc is available at:

```text
http://127.0.0.1:8000/redoc
```

For development with automatic reload:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

---

## 🔐 Environment Configuration

Environment variables are loaded using `python-dotenv`:

```python
from dotenv import load_dotenv

load_dotenv()
```

### Required Configuration

| Variable | Purpose |
| --- | --- |
| `OPENAI_API_KEY` | Authenticate OpenAI model requests |
| `TAVILY_API_KEY` | Authenticate Tavily search requests |
| `AVIATIONSTACK_API_KEY` | Authenticate AviationStack flight requests |
| `AVIATIONSTACK_BASE_URL` | Configure the AviationStack API base URL |
| `DATABASE_URL` | Connect LangGraph to PostgreSQL |
| `DEFAULT_ORIGIN_IATA` | Configure a default departure airport where needed |

Example:

```dotenv
OPENAI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
AVIATIONSTACK_API_KEY=your_key_here
AVIATIONSTACK_BASE_URL=https://api.aviationstack.com/v1
DATABASE_URL=postgresql://username:password@host/database?sslmode=require
DEFAULT_ORIGIN_IATA=CMB
```

**Never commit real API credentials to GitHub.**

An optional `.env.example` can contain placeholders only.

---

## 🌐 FastAPI Endpoints

### Home

```http
GET /
```

Serves the Travexa AI interface through Jinja2.

### Generate Travel Plan

```http
POST /api/travel
```

Example request:

```json
{
  "message": "Plan a 7-day Japan trip from Sri Lanka under 3 lakhs.",
  "thread_id": null
}
```

Successful response structure:

```json
{
  "success": true,
  "thread_id": "user_...",
  "answer": "Final AI travel plan...",
  "flight_results": "Flight information...",
  "hotel_results": "Hotel information...",
  "itinerary": "Generated itinerary...",
  "llm_calls": 4
}
```

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok",
  "message": "AI Travel Planner API is running"
}
```

---

## 🎨 Frontend and Animations

Travexa AI uses a custom dark interface with purple and magenta neon styling.

### 3D Travel Experience

The interface includes:

- 3D-style AI travel globe.
- Orbital rings.
- Floating aircraft.
- Globe longitude and latitude lines.
- Purple neon lighting.
- Animated glow effects.
- Floating travel-information cards.
- Animated background gradients.
- Star effects.
- Mouse-based 3D movement.
- Interactive planner-card tilt.

### Travel Planner

The central planning interface includes:

- Natural-language travel input.
- AI Online indicator.
- Generate AI Trip button.
- Quick travel prompts.
- Animated processing status.
- Generated travel-plan workspace.
- Copy functionality.
- PDF export.

### Processing Indicators

While the backend is processing a request, the frontend cycles through messages such as:

```text
Analyzing your travel request...
Searching for the best travel options...
Checking flights and destinations...
Researching hotels and accommodation...
Building your personalized itinerary...
Optimizing your travel plan...
Preparing your Travexa AI experience...
```

These labels represent frontend activity states while Travexa AI processes the request.

### Markdown Rendering

The frontend uses **Marked** to render Markdown-formatted AI responses inside the result workspace.

### Responsive Design

The interface adapts to desktop, tablet, and mobile layouts.

---

## 📥 Exporting Results

### Copy Travel Plan

Users can copy the generated travel plan directly from the result interface.

### PDF Export

Travexa AI uses `html2pdf.js` to export the rendered travel plan.

The generated filename is:

```text
Travexa-AI-Travel-Plan.pdf
```

---

## 💬 Example Prompts

### 🇬🇧 England

> Plan a complete 7-day England trip from Sri Lanka including flights, hotels and sightseeing under 3 lakhs.

### 🇯🇵 Japan

> Plan a 7-day Japan trip from Sri Lanka under 3 lakhs including flights, hotels, food and sightseeing.

### 🇦🇪 Dubai

> Create a complete Dubai travel plan from Sri Lanka with flights, hotels, attractions and an estimated budget.

### 🇹🇭 Thailand

> Plan a Thailand vacation from Sri Lanka including flights, hotels, sightseeing and a day-by-day itinerary.

### 🇮🇹 Italy

> Plan a 10-day Italy trip from Sri Lanka including Rome, Florence, Venice and Milan.

### ✈️ Flight Search

> Give me flight information from Sri Lanka to Italy.

### 🌍 General Travel Planning

> Create a complete international travel plan including flights, hotels, sightseeing and estimated costs.

---

## 🧩 Error Handling

Travexa AI includes request validation and backend exception handling.

Possible failures include:

- Missing OpenAI API credentials.
- Missing Tavily API credentials.
- Missing AviationStack credentials.
- Invalid PostgreSQL connection information.
- PostgreSQL SSL configuration problems.
- External API failures.
- Provider rate or usage limits.
- Network errors.
- Unavailable model access.
- Missing flight information.
- Missing ticket-price information.
- Empty user requests.

Empty requests return HTTP `400`:

```json
{
  "success": false,
  "error": "Message cannot be empty."
}
```

Unexpected backend failures return HTTP `500`:

```json
{
  "success": false,
  "error": "..."
}
```

Detailed exceptions are also printed in the server terminal using:

```python
traceback.print_exc()
```

---

## ⚠️ Current Limitations

- Flight information depends on data returned by AviationStack.
- Flight results may not include live ticket prices.
- Hotel suggestions use Tavily search rather than direct hotel inventory.
- Travexa AI does not currently book flights.
- Travexa AI does not currently book hotels.
- Generated budgets are planning estimates rather than guaranteed prices.
- Currency rates, hotel prices, and travel costs can change.
- External API availability can affect travel-plan generation.
- The current graph follows a fixed sequential workflow.
- The application does not currently provide user authentication.
- `thread_id` separates LangGraph checkpoint threads but is not an authentication mechanism.
- AI-generated travel plans should be verified before important travel decisions.
- Visa, immigration, health, and entry requirements should be checked through appropriate official sources.

Public production deployment would require additional authentication, authorization, rate limiting, security controls, monitoring, and production-ready concurrency handling.

---

## 🎯 Project Objectives

- Build an end-to-end AI travel-planning application.
- Design a multi-agent workflow using LangGraph.
- Separate travel-planning responsibilities into specialized agents.
- Integrate external flight information.
- Retrieve flight data using AviationStack.
- Research hotel information using Tavily.
- Generate personalized itineraries using an LLM.
- Generate structured final travel plans.
- Maintain graph checkpoints using PostgreSQL.
- Build a FastAPI application around the AI workflow.
- Connect the backend to an interactive JavaScript frontend.
- Create a modern AI-focused travel interface.
- Demonstrate practical agentic AI engineering through a portfolio project.

---

## 📚 Learning Areas

### 🐍 Python

- Modular application development.
- Typed state management.
- External API integration.
- Environment-variable configuration.
- Exception handling.
- UUID-based thread identifiers.
- Reusable travel tools.

### 🦜 LangChain and LangGraph

- LangChain model integration.
- LangGraph `StateGraph`.
- Multi-node workflows.
- Shared graph state.
- Sequential graph execution.
- Message accumulation.
- Persistent checkpoints.
- Thread-based graph configuration.

### 🤖 Large Language Models

- System prompting.
- Structured travel prompts.
- Context aggregation.
- Itinerary generation.
- Final-answer synthesis.
- Combining external information with LLM generation.

### ✈️ Travel APIs

- Flight-data retrieval.
- Airport resolution.
- Country and city processing.
- AviationStack integration.
- Travel-search integration.

### 🔎 Web Search

- Tavily search integration.
- Hotel research.
- External travel-information retrieval.

### 🐘 PostgreSQL

- PostgreSQL connections.
- Psycopg.
- SSL database connections.
- LangGraph `PostgresSaver`.
- Persistent graph checkpoints.

### 🌐 FastAPI

- HTTP routes.
- Pydantic request models.
- JSON responses.
- Jinja2 templates.
- Static-file serving.
- Error handling.
- Health-check endpoints.

### 🎨 Frontend Development

- HTML interface development.
- CSS animation.
- Purple neon design.
- Responsive layouts.
- JavaScript Fetch API.
- DOM updates.
- Markdown rendering.
- PDF generation.
- 3D-style mouse interactions.

---

## 🚀 Future Improvements

- [ ] Add direct hotel-booking API integration.
- [ ] Add real-time flight-price providers.
- [ ] Add flight-booking links.
- [ ] Add hotel-booking links.
- [ ] Add destination weather information.
- [ ] Add interactive maps.
- [ ] Add route visualization.
- [ ] Add restaurant recommendations.
- [ ] Add local transportation planning.
- [ ] Add automatic currency conversion.
- [ ] Add visa-information retrieval.
- [ ] Add travel safety information.
- [ ] Add user authentication.
- [ ] Add saved trips.
- [ ] Add trip-history dashboard.
- [ ] Add user travel preferences.
- [ ] Add long-term personalization.
- [ ] Add human-in-the-loop trip approval.
- [ ] Add travel-planning guardrails.
- [ ] Add supervisor-agent routing.
- [ ] Add parallel agent execution where appropriate.
- [ ] Add automated unit and integration tests.
- [ ] Add LangSmith tracing and evaluation.
- [ ] Add token, latency, and API-cost monitoring.
- [ ] Add Docker containerization.
- [ ] Add CI/CD.
- [ ] Add cloud deployment documentation.
- [ ] Add production monitoring.

These are proposed extensions and are not claims about the current implementation.

---

## 🔒 Configuration Hygiene

Keep credentials, virtual environments, caches, and local configuration out of version control:

```gitignore
# Environment variables
.env
.env.*
!.env.example

# Virtual environments
travexa-env/
.venv/
venv/

# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

Never commit:

```text
OPENAI_API_KEY
TAVILY_API_KEY
AVIATIONSTACK_API_KEY
DATABASE_URL
```

If a secret has already been committed, adding `.env` to `.gitignore` does not remove it from Git history. Revoke the exposed credential and replace it.

---

## ⭐ Project Highlights

### 🤖 Multi-Agent Travel Planning

Travexa AI separates the travel-planning process into specialized LangGraph nodes for flights, hotels, itinerary generation, and final-response synthesis.

### ✈️ Flight Information Integration

AviationStack connects the travel workflow to external flight information.

### 🏨 AI-Assisted Hotel Research

Tavily provides external hotel and destination information for the Hotel Agent.

### 🗺️ Personalized Itinerary Generation

The Itinerary Agent combines the original travel request with retrieved flight and hotel information to create a practical travel plan.

### 🐘 Persistent LangGraph State

PostgreSQL-backed `PostgresSaver` provides graph checkpoint persistence using conversation-specific thread identifiers.

### 🌐 Full-Stack AI Application

FastAPI connects the LangGraph backend to a custom HTML, CSS, and JavaScript frontend.

### 🎨 3D Purple Neon Interface

The Travexa AI interface combines travel-focused animations, neon-purple styling, 3D interactions, activity indicators, and formatted AI results.

### 📄 Reusable Travel Plans

Generated travel plans can be copied or exported as PDF documents.

### 🧩 Modular Architecture

Flight tools, web search, graph orchestration, API routes, frontend markup, styling, and JavaScript interactions are separated into dedicated modules.

---

## 📌 Repository

**[Travexa AI — End-to-End Multi-Agent AI Travel Planner](https://github.com/sudeeraattanayake/Travexa-AI-Multi-Agent-Travel-Planner)**

---

## 👨‍💻 Author

**Sudeera Attanayake**

Generative AI | LLM Applications | AI Agents | Python

**[GitHub Profile](https://github.com/sudeeraattanayake)**

---

## 🤝 Support

If you find this project useful:

- ⭐ Star the repository.
- 🐛 Report issues.
- 💡 Suggest improvements.
- 📚 Explore the implementation.

---

<p align="center">
  <strong>
    Built with 🐍 Python + 🦜 LangGraph + 🤖 OpenAI + ✈️ AviationStack + 🔎 Tavily + 🐘 PostgreSQL + 🌐 FastAPI
  </strong>
</p>

<p align="center">
  <strong>✦ Travexa AI — Plan Smarter. Travel Further.</strong>
</p>
