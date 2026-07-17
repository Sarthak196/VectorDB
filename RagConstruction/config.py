from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(Path(__file__).with_name(".env"))  # Load this app's .env file
# Retrieve the API key from environment variables
API_KEY = os.getenv("API_KEY")
QDRANT_HOST = os.getenv("QDRANT_HOST")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
LLM_MODEL = os.getenv("LLM_MODEL")
PROJECT_NAME = os.getenv("PROJECT_NAME")
DOCUMENTS_PATH = os.getenv("DOCUMENTS_PATH")
