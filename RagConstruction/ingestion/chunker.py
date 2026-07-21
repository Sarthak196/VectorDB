import re

def split_into_sentences(text: str):
    """
    Uses regex to split the text into sentences based on punctuation marks.
    param text: The input text to be split into sentences.
    return: A list of sentences.
    """

    # Regex pattern to match sentence-ending punctuation followed by whitespace or end of string
    pattern = r'(?<=[.!?])\s+'
    sentences = re.split(pattern, text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def create_chunks(text: str, chunk_size: int = 2, overlap: int = 1):
    """
    Chunks the text into smaller pieces with a specified size and overlap.
    param text: The input text to be chunked.
    param chunk_size: The number of sentences per chunk.
    param overlap: The number of sentences to overlap between chunks.
    return: A list of chunks.
    """
    sentences = split_into_sentences(text)
    chunks = []
    for i in range(0, len(sentences), chunk_size - overlap):
        chunk = sentences[i:i+chunk_size]
        chunks.append({
            "text": " ".join(chunk),
            "start": i,
            "end": i + len(chunk) - 1
        })
    return chunks
