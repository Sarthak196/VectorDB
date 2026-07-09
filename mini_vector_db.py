from model import get_model
from sklearn.metrics.pairwise import cosine_similarity

def create_cosine_similarity_matrix(query, db_vectors):
    """
    Create a cosine similarity matrix between a query and a database of documents.

    Args:
        query (str): The query string.
        db_vectors (numpy.ndarray): A 2D array of document vectors.
    Returns:
        numpy.ndarray: A 2D array containing cosine similarity scores.
    """
    query_vector = model.encode([query])
    scores = cosine_similarity(query_vector, db_vectors)
    return scores

model = get_model("all-MiniLM-L6-v2")
documents = [
    "Python is a programming language",
    "FastAPI is a web framework",
    "PostgreSQL is a relational database",
    "Qdrant is a vector database",
    "Dogs are loyal pets"
]
vector = model.encode(documents)
print(f"Vector shape: {vector.shape}")

query_1 = "semantic search database"
scores = create_cosine_similarity_matrix(query_1, vector)
print(f"Scrores for query '{query_1}': {scores}")
print("Best match:", documents[scores.argmax()])

query_2 = "backend web api"
scores = create_cosine_similarity_matrix(query_2, vector)
print(f"Scrores for query '{query_2}': {scores}")
print("Best match:", documents[scores.argmax()])

query_3 = "pet animal"
scores = create_cosine_similarity_matrix(query_3, vector)
print(f"Scrores for query '{query_3}': {scores}")
print("Best match:", documents[scores.argmax()])

query_4 = "sql database"
scores = create_cosine_similarity_matrix(query_4, vector)
print(f"Scrores for query '{query_4}': {scores}")
print("Best match:", documents[scores.argmax()])