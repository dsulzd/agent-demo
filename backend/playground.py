from agno.playground import Playground

from agents.web_agent import web_agent
from agents.research_agent import research_agent
from agents.level_4_team import reasoning_finance_team

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

playground = Playground(
    teams=[reasoning_finance_team],
    agents=[web_agent, research_agent])
app = playground.get_app()

if __name__ == "__main__":
    playground.serve("playground:app", reload=True)