from crewai import Agent, Task
from core.tools import llm, WikipediaSearchTool
from crewai.tools import BaseTool
from utils.fact_memory import query_facts, store_fact

wikipedia_tool = WikipediaSearchTool(
    name="Wikipedia Search Tool",
    description="Looks up and summarizes Wikipedia articles related to a given topic."
)

validator_agent = Agent(
    role="Fact Validator",
    goal="Verify factual claims made in the research brief using public knowledge bases and trusted datasets",
    backstory=(
        "You are a precise and impartial fact-checker. You verify names, dates, events, and statistics using tools like Wikipedia, Wikidata, and trusted APIs.\n"
        "You identify inconsistencies, missing sources, or doubtful claims, and provide a confidence rating (High/Medium/Low) for each fact.\n"
        "You also note if different sources contradict each other. You also use memory to avoid redundant validations."
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
            "Validate the facts in the research brief:\n"
            "- First, check if a similar fact exists in memory using semantic search\n"
            "- If found with high similarity, reuse and mark it as 'memory validated'\n"
            "- If not found, validate using Wikipedia and public web sources\n"
            "- If unconfirmed, mark as 'unverifiable' and add a note\n"
            "- Add a confidence rating and source\n"
            "- Store new validated facts in memory for future reuse"
        ),
        expected_output=(
            "A list of facts with the following format:\n"
            "- Fact: <the fact>\n"
            "- Source: <URL or tool used>\n"
            "- Confidence: High / Medium / Low\n"
            "- Notes: (e.g., 'from memory', 'newly verified', or 'not found')"
        ),
        agent=validator_agent
)
