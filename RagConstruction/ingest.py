from ingestion.pdf_loader import load_pdf
from ingestion.chunker import split_into_sentences, create_chunks
from ingestion.cleaner import clean_text
from ingestion.id_generator import generate_chunk_id
from embed import get_embedding
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from config import QDRANT_HOST


client = QdrantClient(
    url=QDRANT_HOST,
    port=None,
    timeout=20,
    headers={"ngrok-skip-browser-warning": "true"},
)

def ingest_pdf(file_path: str):
    pages = load_pdf(file_path)
    points = []
    point_id = 0

    for page in pages:
        cleaned_text = clean_text(page["text"])
        chunks = create_chunks(cleaned_text, chunk_size=8, overlap=2)
        for chunk in chunks:
            chunk_index = generate_chunk_id(file_path, page["page"], chunk["text"])
            embedding = get_embedding(chunk["text"])
            point = PointStruct(
                id=point_id,
                vector=embedding,
                payload={
                    "document": file_path,
                    "page": page["page"],
                    "chunk_index": chunk_index,
                    "text": chunk["text"],
                    "start": chunk["start"],
                    "end": chunk["end"],
                }
            )
            points.append(point)
            point_id += 1

    client.upsert(
        collection_name="documents",
        points=points
    )

    print(f"Successfully ingested {len(points)} points from {file_path} into Qdrant.")
