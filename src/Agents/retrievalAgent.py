from agno.models.openai import OpenAIChat
from agno.agent import Agent
from pathlib import Path
from dotenv import load_dotenv
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools.web_search_tool import web_search_tool
from tools.qdrant_search_tool import qdrant_search_tool, list_qdrant_collections

load_dotenv()  # Load environment variables from .env file


retrieval_agent = Agent(
    # model = "openai:gpt-4o-mini",
    model = OpenAIChat(id="gpt-4o-mini"),
    name = "RetrievalAgent",
    description = "An agent that retrieves information from Qdrant or the web based on user queries.",
    instructions = """You are a retrieval specialist for a book database system.

CONTEXT: The Qdrant database contains collections of books organized by genre. Each book has metadata including title, author, description, content, genre, and publication details.

YOUR TASK:
- Search the appropriate book collection based on the user's query
- List available collections if requested
- Retrieve relevant book information to answer questions about books, authors, or genres
- Use the exact collection_name provided by the router
- Return comprehensive information about the books found

IMPORTANT:
- Collections are organized by genre (fiction, non-fiction, science_fiction, mystery, etc.)
- Each search result contains book metadata that should be passed to the generation agent
- If the user's question is not related to books or authors, use web_search_tool and nothing else rather than using memory or hallucinate
""",
    tools=[qdrant_search_tool, list_qdrant_collections, web_search_tool],
    # add_history_to_context=False,
    debug_mode=False
)