from crewai import Agent, Task
from core.tools import llm
from utils.fact_memory import query_facts, store_fact
from core.tools import WikipediaSearchTool

wikipedia_tool = WikipediaSearchTool(
    name="Wikipedia Search Tool",
    description="Looks up and summarizes Wikipedia articles related to a given topic."
)

validator_agent = Agent(
    role="Fact Validator",
    goal="Validate every claim strictly against verified sources and previously stored memory",
    backstory=(
        "You're a professional fact-checker. You DO NOT assume or guess.\n"
        "Your job is to confirm if a fact exists in prior memory or on Wikipedia.\n"
        "If it’s not in memory and can’t be verified on Wikipedia, you reject it as unverifiable.\n"
        "You attach confidence level and reason clearly."
    ),
    tools=[wikipedia_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm
)

def create_validator_task(topic: str) -> Task:
    return Task(
        description=(
            f"**Topic: {topic}**\n"
            "For each research claim provided:\n"
            "1. Check if the claim already exists in memory using semantic search.\n"
            "   - If found with high similarity (score < 0.2), reuse it and mark as 'memory validated'.\n"
            "2. If not found, verify using Wikipedia.\n"
            "   - Only accept if the fact appears directly on the page.\n"
            "   - If not clearly confirmed, mark as 'unverifiable'.\n"
            "3. Add a confidence score (High / Medium / Low) and a short note why.\n"
            "4. All newly validated facts must be stored into memory."
        ),
        expected_output=(
            "A list of validation results for each fact.\n"
            "Each must follow this format:\n"
            "- Fact: <the exact claim>\n"
            "- Source: <memory / Wikipedia / none>\n"
            "- Confidence: High / Medium / Low\n"
            "- Notes: Explanation and reasoning\n"
            "Facts not found in memory or Wikipedia must be rejected."
        ),
        agent=validator_agent
    )
