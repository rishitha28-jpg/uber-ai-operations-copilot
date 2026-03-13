from backend.document_loader import load_documents
from backend.vector_db import add_documents


def ingest():

    print("Loading documents...")

    docs = load_documents("knowledge_base")

    # Extract text content
    texts = [doc["content"] for doc in docs]

    if not texts:
        print("No documents found in knowledge base.")
        return

    print(f"Loaded {len(texts)} documents.")

    print("Adding documents to vector database...")

    add_documents(texts)

    print("Ingestion completed successfully.")


if __name__ == "__main__":
    ingest()