import re

def clean_text(text: str) -> str:
    """
    Basic text cleaning function that removes unwanted characters and normalizes whitespace.
    """

    # Remove multiple spaces, newlines, and tabs
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    text = text.strip()
    return text


# if __name__ == "__main__":
#     text = """
#     This is a sample text with    multiple spaces, newlines, and tabs.
#     Hi                                                  my

#     name      is        Sarthak

#     """
#     print(clean_text(text))