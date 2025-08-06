from crewai import Agent, Task

def create_writer_agent(llm):
    return Agent(
        role="Content Writer",
        goal="Write clear, engaging, and factually accurate blog articles using only verified data",
        backstory=(
            "You are a content specialist with strong editorial integrity. You transform structured, verified data into easy-to-read articles.\n"
            "Your writing avoids fluff and speculation, and highlights the facts using great formatting and flow.\n"
            "You only use facts that have been validated and never add anything extra."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm
)

def create_writer_task(topic: str, agent):
    return Task(
        description=(
            f"**Topic: {topic}**\n"
            "Write a well-structured blog article using only the verified facts provided.\n"
            "- Begin with a strong introduction\n"
            "- Organize with H3 subheadings\n"
            "- Include all inline citations in [Source](URL) format\n"
            "- End with a summary\n"
            "- Use proper Markdown syntax"
        ),
        expected_output=(
            "A polished, markdown-formatted blog article with:\n"
            "- H1 title\n"
            "- Thematic H3 sections\n"
            "- Verified content only\n"
            "- Proper citation format inline\n"
            "- No hallucinated or unsupported info"
        ),
        agent=agent
)
