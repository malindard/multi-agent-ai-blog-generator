from crewai import Agent, Task
from crewai_tools import SerperDevTool
from core.tools import llm

search_tool = SerperDevTool(n_results=10)

research_agent = Agent(
    role="Research Analyst",
    goal="Collect trustworthy and diverse information about a given topic using reputable sources",
    backstory=(
        "You're an expert researcher trained in journalism and data analysis. You specialize in sourcing factual, non-biased information from reliable websites.\n"
        "You know how to discard promotional, speculative, or low-quality content. Your goal is to provide structured, evidence-rich research with citations for use in publication-grade writing."
    ),
    tools=[search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm
)

def create_research_task(topic: str) -> Task:
    return Task(
        description=(
            f"**Topic: {topic}**\n"
            "Perform deep research on the provided topic.\n"
            "- Summarize factual findings only (no opinions)\n"
            "- Prioritize official, academic, or authoritative sources\n"
            "- List verified facts with proper context\n"
            "- Provide direct source links next to each claim\n"
            "- Structure the result into thematic sections (e.g., Background, Timeline, People Involved, etc.)"
        ),
        expected_output=(
            "A clean research brief in bullet-point format, containing only verified and sourced information.\n"
            "- Each point must include a [Source](URL) citation.\n"
            "- Avoid redundant data and vague statements.\n"
            "- Group similar facts into clearly labeled sections."
        ),
        agent=research_agent
    )
