from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from model import get_model

client = QdrantClient(
    host="localhost",
    port=6333
)

# Only create collection if it doesn't exist (important for external clients)
try:
    client.get_collection(collection_name="documents")
    print("Collection 'documents' already exists.")
except Exception as e:
    if "Not found: Collection `documents` doesn't exist!" in str(e):
        client.create_collection(
            collection_name="documents",
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )
        print("Collection 'documents' created successfully.")
    else:
        raise e
    
print(
    client.get_collections()
)

documents = [
    {"text":"Python is a programming language", "category": "database", "technology": "Python", "difficulty": "beginner"},
    {"text": "FastAPI is a web framework", "category": "framework", "technology": "FastAPI", "difficulty": "beginner"},
    {"text": "PostgreSQL is a relational database", "category": "database", "technology": "PostgreSQL", "difficulty": "beginner"},
    {"text": "Qdrant is a vector database", "category": "database", "technology": "Qdrant", "difficulty": "intermediate"},
    {"text": "Dogs are loyal pets", "category": "home science", "technology": "GK", "difficulty": "beginner"},
    {"text": "There are 8 planets in the solar system", "category": "space science", "technology": "space", "difficulty": "beginner"},
    {"text": "Machine learning is a subset of AI", "category": "AIML", "technology": "AI", "difficulty": "intermediate"},
    {"text": "The Great Wall of China is visible from space", "category": "geography", "technology": "GK", "difficulty": "beginner"},
    {"text": "Water boils at 100 degrees Celsius", "category": "science", "technology": "GK", "difficulty": "beginner"},
    {"text": "The capital of France is Paris", "category": "geography", "technology": "GK", "difficulty": "beginner"}
]

model = get_model("all-MiniLM-L6-v2")
vectors = model.encode([doc["text"] for doc in documents])
# print(f"Vector shape: {vectors.shape}")

points = []
for i, vector in enumerate(vectors):
    points.append(
        PointStruct(
            id=i,
            vector = vector.tolist(),
            payload = {"document": documents[i]["text"], "category": documents[i]["category"],
                    "technology": documents[i]["technology"], "difficulty": documents[i]["difficulty"]}
        )
    )

client.upsert(collection_name="documents", points=points)
print("Points inserted")
print(vectors.shape)

print(client.get_collection("documents"))

# user query
query = "semantic search database"
query_vector = model.encode(query)

# filtering the results based on a specific field in the payload
results = client.query_points(
    collection_name="documents",
    query=query_vector.tolist(),
    query_filter=Filter(
        must=[
            FieldCondition(
                key="technology",
                match=MatchValue(value="PostgreSQL")
            )
        ]
    ),
    limit=3,
)

# checking the result's score and payload
for point in results.points:
    print("-" * 50)
    print(f"Score   : {point.score:.4f}")
    print(f"Payload : {point.payload}")