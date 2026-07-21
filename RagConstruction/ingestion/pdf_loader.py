import fitz
# from ..config import DOCUMENTS_PATH, PROJECT_NAME

def load_pdf(file_path: str) -> list:
    """
    Load a PDF file and extract its text content.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        list: A list of dictionaries containing the text content of each page.
    """
    document = fitz.open(file_path)
    pages = []
    for page_nume, page in enumerate(document, start=1):
        text = page.get_text()
        pages.append({
            "page": page_nume,
            "text": text
        })
    return pages