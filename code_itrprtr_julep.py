
import os
import textwrap
from julep import Client
from dotenv import load_dotenv

from composio_julep import Action, ComposioToolset
    

load_dotenv()
toolset = ComposioToolset()
composio_tools = toolset.get_actions(actions=[Action.CODEINTERPRETER_EXECUTE_CODE])

api_key = os.environ["JULEP_API_KEY"]
base_url = os.environ["JULEP_API_URL"]
# openai_api_key = os.environ["OPENAI_API_KEY"]

client = Client(api_key=api_key, base_url=base_url)



name = "Sawradip"
about = "Sawradip is a software developer with a passion for solving complex problems and a keen interest in AI. You have the ability to write code and execute it."
default_settings = {
    "temperature": 0.7,
    "top_p": 1,
    "min_p": 0.01,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "length_penalty": 1.0,
    "max_tokens": 150,
}

agent = client.agents.create(
    name=name,
    about=about,
    default_settings=default_settings,
    model="gpt-4",
    tools=composio_tools,
)


user = client.users.create(
    name="Jessica",
    about="Tech recruiter specializing in identifying talented developers.",
)

situation_prompt = """Jessica, a tech recruiter, is conducting an interview with Sawradip, a promising software developer. They discuss various technical topics, with a focus on problem-solving and algorithm design.
"""

session = client.sessions.create(
    user_id=user.id, agent_id=agent.id, situation=situation_prompt
)

user_msg = "Can you give me the five largest prime numbers under 10,000, writing a python funtion and executing it. Be sure to return the value."

# user_msg = "What do you like about tech?"

response = client.sessions.chat(
    session_id=session.id,
    messages=[
        {
            "role": "user",
            "content": user_msg,
            "name": "Jessica",
        },
        # {
        #     "role": "user",
        #     "content": "Can you tell me your name?",
        #     "name": "Jessica",
        # }
    ],
    recall=True,
    remember=True,
)

execution_output = toolset.handle_tool_calls(response)
print(execution_output)


# import os
# from dotenv import load_dotenv
# from julep import Client

# # Environment variable setup
# load_dotenv()
# api_key = os.environ["JULEP_API_KEY"]
# base_url = os.environ["JULEP_API_URL"]

# # Client initialization
# client = Client(api_key=api_key, base_url=base_url)

# # Agent creation representing Jessica
# jessica = client.agents.create(
#     name="Jessica",
#     about="Tech recruiter specializing in identifying talented developers.",
#     default_settings={
#         "temperature": 0.7,
#         "top_p": 1,
#         "min_p": 0.01,
#         "presence_penalty": 0,
#         "frequency_penalty": 0,
#         "length_penalty": 1.0,
#         "max_tokens": 150,
#     },
#     model="gpt-4"
# )

# # User creation for Sawradip, the interview candidate
# sawradip_about = "Sawradip is a software developer with a passion for solving complex problems and a keen interest in AI."
# sawradip = client.users.create(
#     name="Sawradip",
#     about=sawradip_about,
# )

# # Interview scenario setup
# interview_prompt = """Jessica, a tech recruiter, is conducting an interview with Sawradip, a promising software developer. They discuss various technical topics, with a focus on problem-solving and algorithm design."""

# # Starting the interview session
# session = client.sessions.create(
#     user_id=sawradip.id, 
#     agent_id=jessica.id, 
#     situation=interview_prompt
# )

# # Sawradip's question about prime numbers
# question = "Can you write a Python function to find the five largest prime numbers under 10,000?"
# response = client.sessions.chat(
#     session_id=session.id,
#     messages=[
#         {
#             "role": "user",
#             "content": question,
#             "name": "Sawradip",
#         }
#     ],
#     recall=True,
#     remember=True,
# )

# # Handling the coding challenge in the interview
# def find_primes(limit):
#     primes = []
#     for num in range(2, limit):
#         if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
#             primes.append(num)
#     return primes[-5:]

# # Printing the solution
# prime_numbers = find_primes(10000)
# print(f"The five largest prime numbers under 10,000 are: {prime_numbers}")
