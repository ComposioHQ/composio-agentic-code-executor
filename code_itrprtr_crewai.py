from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from composio_crewai import ComposioToolset, Action, App

import dotenv 

# Loading the variables from .env file
dotenv.load_dotenv()
llm = ChatOpenAI()
composioToolset = ComposioToolset(actions=[Action.CODEINTERPRETER_EXECUTE_CODE])

crewai_agent = Agent(
    role="Code interpreter Agent",
    goal="""You can write code and execute it""",
    backstory="""You are an intelligent programmer named CodeInterpreter. You are an expert at coding. Your goal is to help me finish a code change.""",
    verbose=True,
    tools=composioToolset,
    llm=llm,
)

task = Task(
    description="Print 5 largest prime number under 10000",
    agent=crewai_agent,
    expected_output="Output of the codeinterpreter action",
)

print(task.execute())


