from crewai import Crew
from agents.research_agent import research_agent, create_research_task
from agents.validator_agent import validator_agent, create_validator_task
from agents.writer_agent import writer_agent, create_writer_task
from agents.citation_agent import citation_agent, create_citation_task

# Define a function to create and run the full crew workflow
def build_truthscribe_crew(topic: str):
    crew = Crew(
        agents=[
            research_agent,
            validator_agent,
            writer_agent,
            citation_agent
        ],
        tasks=[
            create_research_task(topic),
            create_validator_task(topic),
            create_writer_task(topic),
            create_citation_task(topic)
        ],
        verbose=True
    )

    result = crew.kickoff(inputs={"topic": topic})
    return result
