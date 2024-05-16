
import os

import dotenv
from lyzr_automata import Agent, Task
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from lyzr_automata.tasks.task_literals import InputType, OutputType


dotenv.load_dotenv()
from composio_lyzr import Action, ComposioToolset  # noqa: E402


open_ai_text_completion_model = OpenAIModel(
    api_key=os.environ["OPENAI_API_KEY"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


lyzr_agent = Agent(
    role="CodeInterpreter",
    prompt_persona="You are an intelligent programmer named CodeInterpreter. You are an expert at coding. Your goal is to help me finish a code change.",
)

composio_toolset = ComposioToolset()
composio_tool = composio_toolset.get_lyzr_tool(Action.CODEINTERPRETER_EXECUTE_CODE)

task = Task(
    name="Code Execution",
    agent=lyzr_agent,
    tool=composio_tool,
    output_type=OutputType.TEXT,
    input_type=InputType.TEXT,
    model=open_ai_text_completion_model,
    instructions="Print 5 largest prime number under 10000",
    log_output=True,
    enhance_prompt=False,
)

lyzr_output = LinearSyncPipeline(
    name="Composio Lyzr",
    # completion message after pipeline completes
    completion_message="Task completed",
    tasks=[
        # tasks are instance of Task class
        task,
    ],
).run()

print(lyzr_output)