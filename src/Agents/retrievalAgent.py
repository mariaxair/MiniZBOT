from agno.models.openai import OpenAILike
from agno.agent import Agent
from pathlib import Path
from dotenv import load_dotenv
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools.web_search_tool import web_search_tool
from tools.qdrant_search_tool import qdrant_search_tool

load_dotenv()  # Load environment variables from .env file

retrieval_agent = Agent(
    model="openai:gpt-4o-mini",
    name="RetrievalAgent",
    description="An agent that retrieves information from Qdrant based on user queries.",
    instructions="""You are a retrieval agent. Your job is to search for information using the provided tools.

CRITICAL INSTRUCTIONS:
1. When you receive a query with a collection_name, you MUST use the qdrant_search_tool
2. You MUST pass the EXACT collection_name provided to the qdrant_search_tool
3. Do NOT change or interpret the collection_name - use it exactly as given
4. The collection_name parameter is mandatory for qdrant_search_tool

Example: If given query="what is X" and collection_name="yizumi-electrical-docs", 
you must call: qdrant_search_tool(query="what is X", collection_name="yizumi-electric-docs")
""",
    tools=[qdrant_search_tool, web_search_tool],
    debug_mode=True
)