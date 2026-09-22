from crewai import Agent, Task, Crew, LLM

from config import GEMINI_API_KEY, MODEL_NAME


llm = LLM(
    model=MODEL_NAME,
    api_key=GEMINI_API_KEY
)


def ask_question(question):

    agent = Agent(
        role="AI Assistant",
        goal="Answer the user's question clearly and accurately.",
        backstory="You are a helpful general-purpose AI assistant.",
        llm=llm
    )

    task = Task(
        description=question,
        expected_output="A clear and useful answer to the question.",
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task]
    )

    result = crew.kickoff()

    return str(result)