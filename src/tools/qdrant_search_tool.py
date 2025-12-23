from agno.tools import tool
import os
from dotenv import load_dotenv
from openai import OpenAI
from qdrant_client import QdrantClient

load_dotenv()

# Use official OpenAI client for embeddings
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_HOST"),
    api_key=os.getenv("QDRANT_API_KEY")
)

# Global variable to store the collection name
_CURRENT_COLLECTION = None

def set_collection_name(collection_name: str):
    global _CURRENT_COLLECTION
    print(f"DEBUG: before assignment: {_CURRENT_COLLECTION}")
    _CURRENT_COLLECTION = collection_name
    print(f"DEBUG: after assignment: {_CURRENT_COLLECTION}")

@tool
def qdrant_search_tool(query: str, collection_name: str) -> list:
    if not collection_name:
        raise ValueError("Collection name must be provided")
    
    # Create embedding
    embedding_resp = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )
    embedding = embedding_resp.data[0].embedding

    try:
        search_result = qdrant_client.query_points(
            collection_name=collection_name,
            query=embedding,
            limit=3
        )
        return [hit.payload for hit in search_result.points]
    except Exception as e:
        print(f"❌ Qdrant search error: {e}")
        return [{"error": str(e)}]