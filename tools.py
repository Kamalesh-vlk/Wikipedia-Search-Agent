#tools.py 
from langchain.tools import tool
import wikipedia

@tool
def search_wikipedia(query:str) -> str:
    """Search and return Wikipedia Summary for a given Query."""
    return wikipedia.summary(query, sentences = 5)