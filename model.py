from sentence_transformers import SentenceTransformer
import time

def get_model(model_name):
    """
    Load the SentenceTransformer model with retry logic.

    Args:
        model_name (str): The name of the model to load.

    Returns:
        SentenceTransformer: The loaded model.
    """
    max_retries = 3
    for attempt in range(max_retries):
        try:
            model = SentenceTransformer(model_name)
            print("Model loaded successfully")
            return model
        except RuntimeError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in 2 seconds...")
                time.sleep(2)
            else:
                print("Failed to load model after all retries")
                raise
