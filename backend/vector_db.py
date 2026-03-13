# from typing import List
# import chromadb
# from backend.embeddings import create_embeddings

# # --------------------------------
# # Persistent Vector Database
# # --------------------------------
# client = chromadb.PersistentClient(path="vector_store")

# collection = client.get_or_create_collection(
#     name="uber_support"
# )


# # --------------------------------
# # Document Chunking
# # --------------------------------
# def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:

#     chunks = []
#     start = 0

#     while start < len(text):

#         end = start + chunk_size
#         chunks.append(text[start:end])

#         start += chunk_size - overlap

#     return chunks


# # --------------------------------
# # Add Documents to Vector DB
# # --------------------------------
# def add_documents(texts: List[str]):

#     all_chunks = []
#     ids = []

#     doc_id = 0

#     for text in texts:

#         chunks = chunk_text(text)

#         for chunk in chunks:

#             all_chunks.append(chunk)
#             ids.append(str(doc_id))

#             doc_id += 1

#     embeddings = create_embeddings(all_chunks)

#     collection.add(
#         documents=all_chunks,
#         embeddings=embeddings,
#         ids=ids
#     )


# # --------------------------------
# # Search Vector Database
# # --------------------------------
# def search(query: str, top_k: int = 3) -> List[str]:

#     query_embedding = create_embeddings([query])[0]

#     results = collection.query(
#         query_embeddings=[query_embedding],
#         n_results=top_k
#     )

#     return results["documents"][0]
from typing import List, Dict
import chromadb
from backend.embeddings import create_embeddings

# --------------------------------
# Persistent Vector Database
# --------------------------------
client = chromadb.PersistentClient(path="vector_store")

collection = client.get_or_create_collection(
    name="uber_support"
)


# --------------------------------
# Document Chunking
# --------------------------------
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:

    chunks = []
    start = 0

    while start < len(text):

        end = start + chunk_size
        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


# --------------------------------
# Add Documents to Vector DB
# --------------------------------
def add_documents(texts: List[str]):

    all_chunks = []
    ids = []

    doc_id = 0

    for text in texts:

        chunks = chunk_text(text)

        for chunk in chunks:

            all_chunks.append(chunk)
            ids.append(str(doc_id))

            doc_id += 1

    embeddings = create_embeddings(all_chunks)

    collection.add(
        documents=all_chunks,
        embeddings=embeddings,
        ids=ids
    )


# --------------------------------
# Original Search (UNCHANGED)
# --------------------------------
def search(query: str, top_k: int = 3) -> List[str]:

    query_embedding = create_embeddings([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]


# --------------------------------
# New Search with Sources
# --------------------------------
def search_with_sources(query: str, top_k: int = 3) -> Dict:

    query_embedding = create_embeddings([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return {
        "documents": results["documents"][0],
        "ids": results["ids"][0]
    }