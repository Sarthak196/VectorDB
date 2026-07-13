from google import genai
from config import API_KEY, LLM_MODEL

client = genai.Client(api_key=API_KEY)


def ask_llm(question: str, context: str):

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

Do not use outside knowledge.

If the answer is not present in the context, reply exactly:

"I don't have enough information from the provided documents."

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model=LLM_MODEL,
        contents=prompt,
    )

    return response.text