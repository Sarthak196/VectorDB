from model import get_model
from config import EMBEDDING_MODEL

model = None

def get_embedding(text: str) -> list:
    global model

    if model is None:
        model = get_model(EMBEDDING_MODEL)

    return model.encode(text).tolist()  # Convert the numpy array to a list for easier handling
