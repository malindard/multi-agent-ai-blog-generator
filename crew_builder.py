from crewai import Crew
from agents.research_agent import create_research_agent, create_research_task
from agents.validator_agent import create_validator_agent, create_validator_task
from agents.writer_agent import create_writer_agent, create_writer_task
from agents.citation_agent import create_citation_agent, create_citation_task

# Define a function to create and run the full crew workflow
def build_truthscribe_crew(topic: str, llm):
    # Create agents with the selected LLM
    research_agent  = create_research_agent(llm)
    validator_agent = create_validator_agent(llm)
    writer_agent    = create_writer_agent(llm)
    citation_agent  = create_citation_agent(llm)

    # Create tasks using both topic and agent
    research_task  = create_research_task(topic, research_agent)
    validator_task = create_validator_task(topic, validator_agent)
    writer_task    = create_writer_task(topic, writer_agent)
    citation_task  = create_citation_task(topic, citation_agent)

    crew = Crew(
        agents=[research_agent, validator_agent, writer_agent, citation_agent],
        tasks=[research_task, validator_task, writer_task, citation_task],
        verbose=True
    )
    result = crew.kickoff(inputs={"topic": topic})
    return result
