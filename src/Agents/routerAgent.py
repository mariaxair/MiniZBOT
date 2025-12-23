from agno.agent import Agent
import sys 
from pathlib import Path

from dotenv import load_dotenv
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools.qdrant_search_tool import list_qdrant_collections

load_dotenv()  # Load environment variables from .env file

router_agent = Agent(
    model="openai:gpt-4o-mini",
    name="RouterAgent", 
    description="An agent that determines which Qdrant collection to search based on the user's question.",
    instructions="""
        You are a router agent. Your job is to analyze the user's question and determine which Qdrant collection is most appropriate to search.

        INSTRUCTIONS:
        1. First, use list_qdrant_collections to see what collections are available
        2. Based on the question topic, choose the most relevant collection
        3. Return ONLY the collection name as a single word/phrase, nothing else

        Collection Selection Guidelines:
        - If unsure, list the collections and pick the one that seems most relevant

        CRITICAL: Your response should be ONLY the collection name, for example:
        "yizumi-electrical-docs"

        Do not add explanations, just the collection name.""",

    tools=[list_qdrant_collections],
    debug_mode=True,
    markdown = False
)