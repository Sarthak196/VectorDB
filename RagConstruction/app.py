from ingest import ingest_pdf
from config import DOCUMENTS_PATH

if __name__ == "__main__":
    menu = """
    Welcome to the PDF Ingestion and Retrieval System!
    Please choose an option:
        1. Ingest a PDF file
        2. Retrieve documents based on a query
        3. Exit
    """
    print(menu)
    option = input("Enter your choice (1-3): ")
    if option == "1":
        FILE_PATH = f"{DOCUMENTS_PATH}"
        file_name = input(f"Enter the PDF file name: ")
        ingest_pdf(f"{FILE_PATH}/{file_name}")
    elif option == "2":
        from rag import ask_question
        while True:
            query = input("Enter your query (or 'q' to quit): ")
            if query.lower() == 'q':
                break
            results = ask_question(query)
            print(f"Question: {query}")
            print(f"Answer  : {results}")
            print("*" * 20)
    else:
        print("Exiting the program. Goodbye!")