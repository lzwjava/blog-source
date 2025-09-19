import os
from tavily import TavilyClient

# Retrieve the API key from the environment variable
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if TAVILY_API_KEY is None:
    raise ValueError(
        "API key not found. Please set the TAVILY_API_KEY environment variable."
    )

# Initialize the TavilyClient with the retrieved API key
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# Make a search request
response = tavily_client.search("Who is Leo Messi?")

# Print the response
print(response)
