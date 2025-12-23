from agno.models.openai import OpenAILike
from agno.agent import Agent
from pathlib import Path
from dotenv import load_dotenv
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools.web_search_tool import web_search_tool
from tools.qdrant_search_tool import qdrant_search_tool, list_qdrant_collections

load_dotenv()  # Load environment variables from .env file

retrieval_agent = Agent(
    model="openai:gpt-4o-mini",
    name="RetrievalAgent",
    description="An agent that retrieves information from Qdrant based on user queries.",
    instructions="""
        You are a retrieval agent. Your job is to search for information using the provided tools.

        INSTRUCTIONS:
        1. You will receive a query and a collection_name
        2. Use qdrant_search_tool with the EXACT collection_name provided
        3. Do NOT change or modify the collection_name
        4. If Qdrant search fails, you can fallback to web_search_tool

        Example: If given query="what is X" and collection_name="yizumi-electrical-docs",
        call: qdrant_search_tool(query="what is X", collection_name="yizumi-electrical-docs")""",
    tools=[qdrant_search_tool, list_qdrant_collections, web_search_tool],
    debug_mode=False
)