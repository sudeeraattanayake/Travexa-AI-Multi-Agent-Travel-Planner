from tools.tavily_tool import tavily_search
from tools.fligth_tool import search_flights

# res = tavily_search("best hotels in sri lanka")
# print(res)

res = search_flights("plan a 7 days japan trip from sri lanka")
print(res)
