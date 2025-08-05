import wikipedia
from crewai import LLM
from crewai.tools import BaseTool

class WikipediaSearchTool(BaseTool):
    name: str = "Wikipedia Search Tool"
    description: str = "Searches and summarizes Wikipedia articles based on a query."

    def _run(self, query: str) -> str:
        try:
            page = wikipedia.page(query, auto_suggest=False)
            return f"{page.title}: {page.summary[:500]}... [Read more]({page.url})"
        except Exception as e:
            return f"Wikipedia lookup failed: {str(e)}"

llm = LLM(
    model="command-r",  # From cohere
    temperature=0.7
)