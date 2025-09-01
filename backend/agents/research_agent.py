from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os

research_agent = Agent(
    name="Research Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[DuckDuckGoTools(search=True, news=True)],
    instructions=["Always use tables to display data"],
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)
