# Ride-Hailing AI Operations Copilot

AI-powered support assistant for ride-hailing platforms built using Retrieval Augmented Generation (RAG).  
The system retrieves information from internal policy documents and generates grounded responses using Google Gemini API.

This project simulates an AI operations copilot used by ride-hailing companies to assist riders and drivers with questions related to pricing, safety, disputes, payments, and platform policies.

---

## Project Overview

Ride-hailing platforms receive thousands of support queries daily.  
This AI Copilot helps automate support by retrieving answers from internal documentation.

The system uses a **RAG architecture**:

User Question  
→ Vector Search  
→ Retrieve Relevant Documents  
→ LLM Generation  
→ Answer with Sources

This ensures answers are grounded in company policies rather than hallucinated.


## Key Features

- AI support assistant for rider and driver queries  
- Retrieval Augmented Generation (RAG) pipeline  
- Vector similarity search using ChromaDB  
- Document embeddings using SentenceTransformers  
- LLM response generation using Gemini API  
- FastAPI backend for AI services  
- Streamlit frontend for interactive chat interface  
- Source attribution for transparency  
- Retrieval metrics for debugging and evaluation  
- Industry-style error handling and fallback responses


## Example Questions the System Can Answer

- How does surge pricing work?  
- Why was I charged a cancellation fee?  
- How do I report a lost item?  
- How can I report a safety issue during a trip?  
- How are driver earnings calculated?  
- When are driver payments processed?  
- How can I dispute a trip charge?


## System Architecture

User Interface (Streamlit)
↓
FastAPI Backend API
↓
RAG Pipeline
├── Vector Search (ChromaDB)
├── Document Embeddings (SentenceTransformers)
↓
Gemini LLM Generation
↓
Final Response + Sources


## Project Structure

uber-ai-operations-copilot
│
├── backend
│ ├── main.py
│ ├── rag_pipeline.py
│ ├── vector_db.py
│ ├── gemini_client.py
│ ├── embeddings.py
│ ├── document_loader.py
│ └── config.py
│
├── frontend
│ └── streamlit_app.py
│
├── scripts
│ └── ingest_data.py
│
├── knowledge_base
│ ├── rider_support.txt
│ ├── driver_payments.txt
│ ├── pricing_policy.txt
│ ├── safety_policy.txt
│ ├── lost_items.txt
│ └── trip_disputes.txt
│
├── requirements.txt
├── .gitignore
└── README.md

## Tech Stack

### Backend
- FastAPI
- Python

### AI / Machine Learning

- Gemini API (LLM)
- SentenceTransformers
- ChromaDB

### Frontend

- Streamlit

### Infrastructure

- Vector database for semantic search
- REST API architecture

## Installation

Clone the repository
git clone https://github.com/rishitha28-jpg/uber-ai-operations-copilot.git
cd uber-ai-operations-copilot
Create virtual environment
python -m venv venv
Activate environment
Windows
venv\Scripts\activate
Install dependencies
pip install -r requirements.txt

## Environment Setup

Create a `.env` file in the project root
GEMINI_API_KEY=your_api_key_here
You can generate an API key from:
https://aistudio.google.com/app/apikey

## Ingest Knowledge Base

Load policy documents into the vector database.
python -m scripts.ingest_data
This step creates embeddings and stores them in ChromaDB.

## Run Backend API

uvicorn backend.main:app --reload
Open API docs:
http://127.0.0.1:8000/docs

## Run Frontend Chat Interface

streamlit run frontend/streamlit_app.py
Open the app in your browser.

## Example API Request

POST /chat
Request body
{
"query": "How does surge pricing work?"
}

Response
{
"answer": "Surge pricing temporarily increases fares during high demand periods.",
"sources": ["12","3","7"],
"retrieval_count": 3
}

## Future Improvements

- Conversation memory for multi-turn chats  
- Knowledge base upload interface  
- Query rewriting for better retrieval  
- Advanced monitoring and logging  
- Deployment with Docker

## Disclaimer

This project is a simulation of an AI support system for educational and portfolio purposes.  
It is not affiliated with any real ride-hailing company.