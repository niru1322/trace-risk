from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

def search_web(query: str):
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    result = client.search(query, max_results=5)
    return result['results']