from crewai import Agent, Task
from crewai_tools import SerperDevTool
from core.tools import llm

search_tool = SerperDevTool(n_results=10)

research_agent = Agent(
    role="Research Analyst",
    goal="Collect trustworthy and diverse information about a given topic using reputable sources",
    backstory=(
        "You're an expert researcher and senior research analyst that trained in journalism and data analysis. You specialize in sourcing factual, non-biased information from reliable websites.\n"
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
            "Perform objective, citation-based research on this topic using web search tools.\n\n"
            "### DO THIS:\n"
            "- Extract only factual, verifiable information\n"
            "- Each fact MUST include a proper [Source](URL) citation — do not omit it\n"
            "- Prioritize trusted sources (Wikipedia, Billboard, official group websites, Forbes, etc.)\n"
            "- Group facts into structured sections using markdown headings:\n"
            "  - ## Background\n"
            "  - ## Formation\n"
            "  - ## Members\n"
            "  - ## Timeline\n"
            "  - ## Reception / Milestones\n\n"
            "### DO NOT DO THIS:\n"
            "- Do NOT invent any names, dates, or events\n"
            "- Do NOT include facts unless the source is explicitly cited\n"
            "- Do NOT summarize opinions or speculation\n"
            "- Do NOT reuse facts unless you found them again with source\n\n"
            "### Tips:\n"
            "- Prefer lists or bullet points when possible\n"
            "- Mention source next to every key claim\n"
            "- If a fact is unverified or unclear, skip it\n"
        ),
        expected_output=(
            "A markdown-formatted research brief grouped into thematic sections. "
            "All facts must include working, trustworthy citations in the format [Source](URL). "
            "There must be no vague statements or hallucinated content. The structure must be clean and factual."
        ),
        agent=research_agent
    )
