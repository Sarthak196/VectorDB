import hashlib
from pathlib import Path

def generate_chunk_id(document_path: str, page_number: int, chunk_text: str) -> str:
    """
    Generates a unique ID for a chunk based on the document path, page number, and chunk text.
    param document_path: The path to the document.
    param page_number: The page number of the document.
    param chunk_text: The text of the chunk.
    return: A unique ID for the chunk.
    """
    # Create a unique string based on document path, page number, and chunk text
    document_name = Path(document_path).name  
    unique_string = f"{document_name}|{page_number}|{chunk_text}"
    
    # Generate a SHA-256 hash of the unique string
    chunk_id = hashlib.sha256(unique_string.encode("utf-8")).hexdigest()
    
    return chunk_id