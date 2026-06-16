from tavily import TavilyClient
from tavily.errors import InvalidAPIKeyError
import os
from dotenv import load_dotenv

load_dotenv()


# https://www.tavily.com/ 
# Signup and login, On dashboard- > under api keys you will see the default key.
# Use that or click on + to create new one. Then save it in .env file

def _get_client():
    api_key = os.getenv("TAVILY_API_KEY", "").strip()
    if not api_key:
        return None
    return TavilyClient(api_key=api_key)

# test it
#################################
# response = client.search(
    # query="Best hotels in Dubai"
# )

# print(response)

####################################



def tavily_search(query):
    client = _get_client()
    if client is None:
        return "Tavily search unavailable: missing TAVILY_API_KEY in .env"

    try:
        response = client.search(
            query=query,
            max_results=5
        )
    except InvalidAPIKeyError:
        return "Tavily search unavailable: invalid TAVILY_API_KEY. Generate a new key from tavily.com and update .env."
    except Exception as exc:
        return f"Tavily search unavailable: {exc}"

    results = []

    for i, r in enumerate(response["results"], 1):
        title   = r.get("title", "Unknown")
        url     = r.get("url", "")
        snippet = r.get("content", "").strip()
        # Keep only the first 300 characters to avoid wall-of-text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results)
    
    
    
