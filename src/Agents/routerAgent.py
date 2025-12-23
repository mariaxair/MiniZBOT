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
    description="An agent that routes book-related queries to the appropriate collection.",
    instructions="""You are a routing specialist for a book database system.

CONTEXT: You work with a database of books organized into collections by genre. Your job is to determine which genre collection best matches the user's question.

AVAILABLE COLLECTIONS:
- Each collection represents a different genre (fiction, mystery, science_fiction, romance, etc.)
- Use list_qdrant_collections to see all available genre collections

YOUR TASK:
1. Analyze the user's question to understand what type of books they're interested in
2. List available collections
3. Choose the most relevant genre collection
4. Return ONLY the exact collection name

EXAMPLES:
- "recommend a sci-fi book" → science_fiction
- "looking for a mystery novel" → mystery
- "what's a good romance book" → romance
- "I want to read fiction" → fiction

CRITICAL: Return ONLY the collection name, nothing else.
""",

    tools=[list_qdrant_collections],
    debug_mode=False,
    markdown = False
)