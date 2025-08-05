from crewai import Agent, Task
from core.tools import llm

citation_agent = Agent(
    role="Citation Cleaner",
    goal="Ensure all citations in the article are valid, working, and properly formatted",
    backstory=(
        "You're an editorial assistant specializing in compliance with citation standards.\n"
        "You scan the article for broken links, bad citation formats, and ensure every source is clean and listed correctly.\n"
        "You also compile a final 'References' section at the end."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

def create_citation_task(topic: str) -> Task:
    return Task(
        description=(
            f"**Topic: {topic}**\n"
            "Review the final markdown article:\n"
            "- Ensure all citations are in [Text](URL) format\n"
            "- Remove broken or unreachable links\n"
            "- Add a bullet-point 'References' section listing all sources at the end\n"
            "- Do not change the article content, only citations"
        ),
        expected_output=(
            "A markdown article with:\n"
            "- Clean inline citations\n"
            "- Functional links only\n"
            "- Bullet list 'References' section with all source links"
        ),
        agent=citation_agent
)
