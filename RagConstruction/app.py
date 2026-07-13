# from retrieve import retrieve_documents
# results = retrieve_documents("semantic search database")

# for result in results:
#     print("-" * 50)
#     print(f"Score   : {result.score:.4f}")
#     print(f"Payload : {result.payload}")

from rag import ask_question
while True:
    question = input("Enter your question (or 'q' to quit): ")
    if question.lower() == 'q':
        break
    answer = ask_question(question)
    print(f"Question: {question}")
    print(f"Answer  : {answer}")
    print("*" * 20)