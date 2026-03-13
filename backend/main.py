# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from backend.rag_pipeline import rag_chat

# app = FastAPI(
#     title="Ride-Hailing AI Operations Copilot API",
#     description="AI-powered support assistant for ride-hailing operations using RAG + Gemini",
#     version="1.0.0"
# )


# class ChatRequest(BaseModel):
#     query: str


# class ChatResponse(BaseModel):
#     response: str


# @app.get("/")
# async def root():
#     return {"message": "Ride-Hailing AI Copilot API running"}


# @app.get("/health")
# async def health_check():
#     return {"status": "ok"}


# @app.post("/chat", response_model=ChatResponse)
# async def chat(request: ChatRequest):

#     try:
#         answer = rag_chat(request.query)

#         return {"response": answer}

#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail=f"Chat processing failed: {str(e)}"
#         )

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from backend.rag_pipeline import rag_chat

app = FastAPI(
    title="Ride-Hailing AI Operations Copilot API",
    description="AI-powered support assistant for ride-hailing operations using RAG + Gemini",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    answer: str
    sources: List[str]
    retrieval_count: int


@app.get("/")
async def root():
    return {"message": "Ride-Hailing AI Copilot API running"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    try:

        result = rag_chat(request.query)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Chat processing failed: {str(e)}"
        )