from griptape.structures import Agent
from griptape.utils import Chat

from composio_griptape import App, Action, Tag, ComposioToolSet
import dotenv


dotenv.load_dotenv()

composio_toolset = ComposioToolSet()
composio_tools = composio_toolset.get_actions(actions=Action.CODEINTERPRETER_EXECUTE_CODE)

agent = Agent(
    tools=composio_tools
)

task = "Print 5 largest prime number under 10000"
print(agent.run(task).output_task.output.value)
