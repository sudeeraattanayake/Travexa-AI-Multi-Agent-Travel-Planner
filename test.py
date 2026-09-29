from tools.tavily_tool import tavily_search
from tools.fligth_tool import search_flights
from backend import run_travel_agent

# res = tavily_search("best hotels in sri lanka")
# print(res)

# res = search_flights("plan a 7 days japan trip from sri lanka")
# print(res)

user_input = input("Enter travel request:")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])
