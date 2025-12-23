from agno.models.openai import OpenAILike
from agno.agent import Agent
from pathlib import Path
from dotenv import load_dotenv
import sys,os
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools.web_search_tool import web_search_tool
from tools.qdrant_search_tool import qdrant_search_tool

load_dotenv()  # Load environment variables from .env file


generating_agent = Agent(
    model="openai:gpt-4o-mini",
    name="GeneratingAgent",
    description="An agent that generates information from Qdrant or web search based on user queries.",
    tools=[qdrant_search_tool, web_search_tool],
    debug_mode=True
)
