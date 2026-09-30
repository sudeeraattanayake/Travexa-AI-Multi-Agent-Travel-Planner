from mcp_client import (
    tavily_mcp_search,
    aviation_mcp_call,
    extract_destination,
    forecast_mcp_search,
    weather_mcp_search,
)

from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AnyMessage,
    HumanMessage,
    AIMessage,
    SystemMessage,
)

from langgraph.graph import StateGraph, START, END

import uuid
import operator
from typing import TypedDict, Annotated
import os
import certifi

from dotenv import load_dotenv


# =========================================================
# Environment Setup
# =========================================================

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is missing. "
        "Please add it to your .env file."
    )


# =========================================================
# LLM
# =========================================================

llm = ChatOpenAI(
    model="gpt-5.6-luna",
    api_key=OPENAI_API_KEY,
)


# =========================================================
# State
# =========================================================

class TravelState(TypedDict):

    messages: Annotated[
        list[AnyMessage],
        operator.add,
    ]

    user_query: str

    flight_results: str
    hotel_results: str
    weather_results: str
    itinerary: str

    llm_calls: int


# =========================================================
# Flight Agent
# =========================================================

FLIGHT_AGENT_PROMPT = """
You are a travel flight expert.

User Query:
{query}

Airport Information:
{airport_data}

Airline Information:
{airline_data}

Generate:
1. Likely departure airport
2. Likely arrival airport
3. Airlines serving this route
4. Typical flight duration
5. Estimated airfare range
6. Peak season pricing warning
7. Booking advice

Return concise travel guidance.
"""


async def flight_agent(
    state: TravelState,
):

    print("\nINSIDE FLIGHT AGENT\n")

    query = state["user_query"]

    try:

        airports = await aviation_mcp_call(
            "list_airports"
        )

        airlines = await aviation_mcp_call(
            "list_airlines"
        )

        print(
            "\nAIRPORTS:",
            airports,
        )

        print(
            "\nAIRLINES:",
            airlines,
        )

        prompt = FLIGHT_AGENT_PROMPT.format(
            query=query,
            airport_data=str(airports)[:3000],
            airline_data=str(airlines)[:3000],
        )

        response = await llm.ainvoke(
            [
                SystemMessage(
                    content=(
                        "You are an expert travel "
                        "flight planner."
                    )
                ),

                HumanMessage(
                    content=prompt
                ),
            ]
        )

        flight_data = response.content

    except Exception as exc:

        print(
            f"FLIGHT AGENT ERROR: "
            f"{type(exc).__name__}: {exc}",
            flush=True,
        )

        flight_data = (
            f"Flight information unavailable: {exc}"
        )

    return {
        "flight_results": flight_data,

        "messages": [
            AIMessage(
                content=(
                    "Flight recommendations generated."
                )
            )
        ],

        "llm_calls": (
            state.get("llm_calls", 0) + 1
        ),
    }


# =========================================================
# Hotel Agent
# =========================================================

async def hotel_agent(
    state: TravelState,
):

    query = (
        f"Best hotels for "
        f"{state['user_query']}"
    )

    try:

        hotel_results = await tavily_mcp_search(
            query
        )

    except Exception as exc:

        print(
            f"HOTEL AGENT ERROR: "
            f"{type(exc).__name__}: {exc}",
            flush=True,
        )

        hotel_results = (
            f"Hotel information unavailable: {exc}"
        )

    return {
        "hotel_results": str(hotel_results),

        "messages": [
            AIMessage(
                content="Hotel information fetched."
            )
        ],

        "llm_calls": (
            state.get("llm_calls", 0) + 1
        ),
    }


# =========================================================
# Weather Agent
# =========================================================

async def weather_agent(
    state: TravelState,
):

    query = state["user_query"]

    try:

        city = await llm.ainvoke(
            f"""
Extract only the destination city or country
from this travel request:

{query}

Return only the destination name.
Do not add any explanation.
"""
        )

        destination = str(
            city.content
        ).strip()

    except Exception:

        destination = extract_destination(
            query
        )

    print(
        f"\nWEATHER DESTINATION: {destination}\n"
    )

    try:

        weather_data = await weather_mcp_search(
            destination
        )

        forecast_data = await forecast_mcp_search(
            destination
        )

        weather_results = f"""
Current Weather:
{weather_data}

Forecast:
{forecast_data}
"""

    except Exception as exc:

        print(
            f"WEATHER AGENT MCP ERROR: "
            f"{type(exc).__name__}: {exc}",
            flush=True,
        )

        weather_results = (
            f"Live weather information for "
            f"{destination} is temporarily unavailable. "
            f"Give general seasonal guidance and advise "
            f"the traveler to verify the forecast "
            f"before departure."
        )

    return {
        "weather_results": weather_results,

        "messages": [
            AIMessage(
                content=(
                    "Weather information processed."
                )
            )
        ],

        "llm_calls": (
            state.get("llm_calls", 0) + 1
        ),
    }


# =========================================================
# Itinerary Agent
# =========================================================

async def itinerary_agent(
    state: TravelState,
):

    prompt = f"""
Create a complete travel itinerary.

User Query:
{state['user_query']}

Flight Results:
{state['flight_results']}

Hotel Results:
{state['hotel_results']}

Weather Results:
{state['weather_results']}

Make the itinerary practical, budget-aware,
weather-aware, and easy to follow.
"""

    response = await llm.ainvoke(
        [
            SystemMessage(
                content=(
                    "You are an expert travel planner."
                )
            ),

            HumanMessage(
                content=prompt
            ),
        ]
    )

    return {
        "itinerary": response.content,

        "messages": [
            response
        ],

        "llm_calls": (
            state.get("llm_calls", 0) + 1
        ),
    }


# =========================================================
# Final Response Agent
# =========================================================

async def final_agent(
    state: TravelState,
):

    final_prompt = f"""
Generate the final travel response for the user.

User Request:
{state['user_query']}

Flights:
{state['flight_results']}

Hotels:
{state['hotel_results']}

Weather:
{state['weather_results']}

Itinerary:
{state['itinerary']}

Format the final answer beautifully using
these sections:

1. Trip Summary
2. Flight Information
3. Hotel Suggestions
4. Weather Information
5. Day-by-Day Itinerary
6. Estimated Budget
7. Final Recommendations

Important:
- Be clear and practical.
- Consider weather conditions when recommending
  activities.
- Mention that live flight API may not provide
  ticket prices if pricing is unavailable.
- Keep the response useful for real travel planning.
"""

    response = await llm.ainvoke(
        [
            SystemMessage(
                content=(
                    "You are a professional AI "
                    "travel booking assistant."
                )
            ),

            HumanMessage(
                content=final_prompt
            ),
        ]
    )

    return {
        "messages": [
            response
        ],

        "llm_calls": (
            state.get("llm_calls", 0) + 1
        ),
    }


# =========================================================
# Build Graph
# =========================================================

graph = StateGraph(
    TravelState
)


graph.add_node(
    "flight_agent",
    flight_agent,
)

graph.add_node(
    "hotel_agent",
    hotel_agent,
)

graph.add_node(
    "weather_agent",
    weather_agent,
)

graph.add_node(
    "itinerary_agent",
    itinerary_agent,
)

graph.add_node(
    "final_agent",
    final_agent,
)


# =========================================================
# Graph Flow
# =========================================================

graph.add_edge(
    START,
    "flight_agent",
)

graph.add_edge(
    "flight_agent",
    "hotel_agent",
)

graph.add_edge(
    "hotel_agent",
    "weather_agent",
)

graph.add_edge(
    "weather_agent",
    "itinerary_agent",
)

graph.add_edge(
    "itinerary_agent",
    "final_agent",
)

graph.add_edge(
    "final_agent",
    END,
)


# =========================================================
# Compile Graph
# =========================================================

# PostgreSQL checkpointer is temporarily disabled.
# Your previous PostgresSaver was synchronous while this
# graph now runs asynchronously with ainvoke().

travel_graph = graph.compile()


# =========================================================
# Function for FastAPI
# =========================================================

async def run_travel_agent(
    user_input: str,
    thread_id: str | None = None,
):

    if not thread_id:

        thread_id = (
            f"user_{uuid.uuid4().hex}"
        )

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    result = await travel_graph.ainvoke(
        {
            "messages": [
                HumanMessage(
                    content=user_input
                )
            ],

            "user_query": user_input,

            "flight_results": "",

            "hotel_results": "",

            "weather_results": "",

            "itinerary": "",

            "llm_calls": 0,
        },

        config=config,
    )

    final_answer = (
        result["messages"][-1].content
    )

    return {
        "thread_id": thread_id,

        "answer": final_answer,

        "flight_results": result.get(
            "flight_results",
            "",
        ),

        "hotel_results": result.get(
            "hotel_results",
            "",
        ),

        "weather_results": result.get(
            "weather_results",
            "",
        ),

        "itinerary": result.get(
            "itinerary",
            "",
        ),

        "llm_calls": result.get(
            "llm_calls",
            0,
        ),
    }
