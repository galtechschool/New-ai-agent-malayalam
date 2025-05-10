from google.adk.tools import google_search
from google.adk.agents import LlmAgent
from .util import load_instruction_from_file

news_agent = LlmAgent(
    name="news_agent",
    model="gemini-2.0-flash-exp",
    description="An agent that searches the latest news and summarizes it in Malayalam",
    instruction=load_instruction_from_file("instructions.txt"),
    tools=[google_search]
)

root_agent = news_agent
 
 