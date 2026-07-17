from retrieve import retrieve_documents
from llm import ask_llm

def build_context(results):
    context = ""
    for i, result in enumerate(results):
        context += (
            f"{i+1}. {result.payload['text']}\n\n"
        )
    return context

def ask_question(question):
    results = retrieve_documents(question)
    context = build_context(results)
    answer = ask_llm(question, context)
    return answer