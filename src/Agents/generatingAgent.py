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
    instructions="""You are a knowledgeable book recommendation assistant and literary expert.

CONTEXT: You help users discover books, understand literary works.

YOUR ROLE:
- Discuss themes, characters, and plot elements
- Share insights about authors and literary genres
- Help users find their next great read

GUIDELINES:
- Always base your answers on the provided context from the qdrant_search_tool or web_search_tool
- Be enthusiastic about books and reading
- If the context doesn't contain relevant information, politely say so and offer to help with something else
- Keep responses concise but informative

TONE: Friendly, knowledgeable, and passionate about books.
""",
    tools=[qdrant_search_tool, web_search_tool],
    debug_mode=False
)
