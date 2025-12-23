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
@tool
def list_qdrant_collections() -> dict:
    """
    list all collections in Qdrant with their description and return as a dict
    Use this to see what collections are available before searching.
    
    Returns:
        Dictionary with collection names and metadata
    """

    try: 
        collections = qdrant_client.get_collections() # retourne un objet qui contient une liste de collections
        result = {}
        for collection in collections.collections: #boucler sur chaque collection trouvee
            # get collection info
            try:
                info = qdrant_client.get_collection(collection.name) # get collection's name ex "yizumi-electrical-docs"
                result[collection.name] = {
                        "points_count": info.points_count, # number of points/docs in the collection
                        "status": info.status # e.g., "green" which means active
                    }
            except Exception as e:
                # If we can't get detailed info, just add the name
                result[collection.name] = {"status": "available"}

        print(f"📚 Available collections: {list(result.keys())}")
        return result
    except Exception as e:
        print(f"❌ Error listing collections: {e}")
        return {"error": str(e)}


@tool
def qdrant_search_tool(query: str, collection_name: str) -> list:
    """
    search for relevant information in a specific qdrant collection.
    
    Args:
    query (str): The search query.
    collection_name: The exact name of the collection to search (use list_qdrant_collections to see available collections)
    

    Returns:
        List of relevant document chunks with their content.
    """

    print(f"🔍 Searching Qdrant collection '{collection_name}' for query: {query}")

    #create embedding for the query
    embedding_response = openai_client.embeddings.create(
        model = "text-embedding-3-large",
        input = query
    )
    embedded_query = embedding_response.data[0].embedding

    try:
        search_result = qdrant_client.query_points(
            collection_name=collection_name,
            query=embedded_query,
            limit=3,
        )
        results = [hit.payload for hit in search_result.points]
        print(f"✅ Found {len(results)} results from Qdrant")
        return results
    except Exception as e:
        print(f"❌ Qdrant search error: {e}")
        return [{"error": f"Collection '{collection_name}' not found or error: {str(e)}"}]