from qdrant_client import QdrantClient
from embed import get_embedding
from config import QDRANT_HOST

client = QdrantClient(
    url=QDRANT_HOST,
    port=None,
    timeout=20,
    headers={"ngrok-skip-browser-warning": "true"},
)

def retrieve_documents(query, limit=3):

    query_vector = get_embedding(query)

    results = client.query_points(
        collection_name="documents",
        query=query_vector,
        limit=limit
    )

    return results.points