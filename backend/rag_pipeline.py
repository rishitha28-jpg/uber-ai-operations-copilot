# from typing import List
# from backend.vector_db import search
# from backend.gemini_client import ask_gemini


# def build_prompt(query: str, context_chunks: List[str]) -> str:
#     """
#     Build the final prompt for the LLM using retrieved context.
#     """

#     # Limit context size to prevent very long prompts
#     context = "\n\n".join(context_chunks[:5])

#     prompt = f"""
# You are an AI operations support assistant for a ride-hailing platform similar to Uber.

# Your role is to help riders and drivers understand platform policies, pricing,
# trip issues, safety concerns, and support processes.

# Instructions:
# - Use ONLY the information provided in the context.
# - Answer clearly and professionally.
# - If the context does not contain the answer, say:
#   "I could not find that information in the support documentation."
# - Do not make up information.

# ---------------------
# Context Information
# ---------------------
# {context}

# ---------------------
# User Question
# ---------------------
# {query}

# Provide a helpful and clear response.
# """

#     return prompt


# def rag_chat(query: str) -> str:
#     """
#     Main RAG pipeline.
#     """

#     # Retrieve relevant documents
#     docs = search(query)

#     if not docs:
#         return "I could not find relevant information in the knowledge base."

#     # Build LLM prompt
#     prompt = build_prompt(query, docs)

#     # Generate answer using Gemini
#     response = ask_gemini(prompt)

#     return response
from typing import List, Dict
from backend.vector_db import search_with_sources
from backend.gemini_client import ask_gemini


def build_prompt(query: str, context_chunks: List[str]) -> str:
    """
    Build the final prompt for the LLM using retrieved context.
    """

    # Limit context size to prevent very long prompts
    context = "\n\n".join(context_chunks[:5])

    prompt = f"""
You are an AI operations support assistant for a ride-hailing platform similar to Uber.

Your role is to help riders and drivers understand platform policies, pricing,
trip issues, safety concerns, and support processes.

Instructions:
- Use ONLY the information provided in the context.
- Answer clearly and professionally.
- If the context does not contain the answer, say:
  "I could not find that information in the support documentation."
- Do not make up information.

---------------------
Context Information
---------------------
{context}

---------------------
User Question
---------------------
{query}

Provide a helpful and clear response.
"""

    return prompt


def rag_chat(query: str) -> Dict:
    """
    Main RAG pipeline.
    """

    try:

        # Retrieve documents + sources
        results = search_with_sources(query)

        docs = results["documents"]
        sources = results["ids"]

        if not docs:
            return {
                "answer": "I could not find relevant information in the knowledge base.",
                "sources": [],
                "retrieval_count": 0
            }

        # Build prompt
        prompt = build_prompt(query, docs)

        # Generate answer
        answer = ask_gemini(prompt)

        return {
            "answer": answer,
            "sources": sources,
            "retrieval_count": len(docs)
        }

    except Exception as e:

        print("RAG pipeline error:", e)

        return {
            "answer": "An error occurred while processing the request.",
            "sources": [],
            "retrieval_count": 0
        }