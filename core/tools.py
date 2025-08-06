import wikipedia
from crewai import LLM
from crewai.tools import BaseTool
from os import getenv

cohere_api_key = getenv("COHERE_API_KEY")

class WikipediaSearchTool(BaseTool):
    name: str = "Wikipedia Search Tool"
    description: str = "Searches and summarizes Wikipedia articles based on a query."

    def _run(self, query: str) -> str:
        try:
            page = wikipedia.page(query, auto_suggest=False)
            return f"{page.title}: {page.summary[:500]}... [Read more]({page.url})"
        except Exception as e:
            return f"Wikipedia lookup failed: {str(e)}"

def get_llm(temperature: float):
    return LLM(
        provider="cohere",
        model="command-r",
        api_key=cohere_api_key,
        temperature=temperature
    )