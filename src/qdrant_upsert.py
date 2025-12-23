import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

# Charger variables d'environnement
load_dotenv()

# Init OpenAI et Qdrant
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_HOST"),
    api_key=os.getenv("QDRANT_API_KEY")
)

# Charger ton JSON de livres
with open("../books.json", "r", encoding="utf-8") as f:
    books = json.load(f)

# Group books by genre (handle list of genres)
books_by_genre = {}
for book in books:
    for genre in book.get("genre", ["Unknown"]):  # loop through each genre
        key = genre.replace(" ", "_").lower()      # normalize collection name
        if key not in books_by_genre:
            books_by_genre[key] = []
        books_by_genre[key].append(book)

# 4️⃣ For each genre, create collection and upsert books
for genre_key, books_in_genre in books_by_genre.items():
    
    collection_name = genre_key  # already normalized
    
    # Create collection if it doesn't exist
    existing_collections = [c.name for c in qdrant_client.get_collections().collections]
    if collection_name not in existing_collections:
        qdrant_client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=3072, distance=Distance.COSINE)
        )
    
    points = []
    for book in books_in_genre:
        content = book.get("content", book.get("description", ""))
        embedding_response = openai_client.embeddings.create(
            model="text-embedding-3-large",
            input=content
        )
        vector = embedding_response.data[0].embedding
        points.append(PointStruct(
            id=book["id"],
            vector=vector,
            payload=book  # store entire book metadata as payload
        ))
    
    # Upsert points
    qdrant_client.upsert(
        collection_name=collection_name,
        points=points
    )
    print(f"✅ Upserted {len(points)} books into collection '{collection_name}'")
