# Insurance AI Copilot

## Overview

Insurance AI Copilot is an AI-powered conversational insurance assistant developed using FastAPI, Streamlit, LangChain, OpenAI, Pinecone, and Retrieval-Augmented Generation (RAG).

The application is designed to assist users with:

* Insurance policy recommendations
* Policy comparison
* Premium estimation
* Coverage explanation
* Waiting period and exclusion analysis
* Intelligent insurance-related conversations
* Context-aware follow-up interactions
* Retrieval of policy-specific information using RAG

The system follows a modular and scalable architecture suitable for AI-based enterprise applications.

---

# Project Objectives

The primary objective of this project is to build an intelligent insurance assistant capable of:

1. Understanding natural language insurance queries
2. Retrieving accurate policy-related information
3. Reducing hallucinations using RAG architecture
4. Providing structured and contextual responses
5. Maintaining conversation continuity
6. Delivering a modern interactive user experience

---

# Technologies Used

## Programming Language

* Python 3.11

## Backend Framework

* FastAPI
* Uvicorn

## Frontend Framework

* Streamlit

## AI / LLM Technologies

* OpenAI GPT-4.1-mini
* OpenAI Embedding Models
* LangChain

## Vector Database

* Pinecone

## Retrieval Technologies

* FAISS
* BM25 Retrieval
* Sentence Transformers

## Document Processing

* PyMuPDF
* PaddleOCR
* PaddlePaddle

## Additional Libraries

* Pydantic
* NumPy
* PyYAML
* Python-dotenv
* HTTPX
* Pytest

---

# System Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ▼
Main Chatbot Orchestrator
  │
  ├── Guardrails Validation
  ├── Query Classification
  ├── Conversation Memory
  ├── Structured Knowledge Lookup
  ├── RAG Retrieval Pipeline
  │      ├── OpenAI Embeddings
  │      ├── Pinecone Vector Search
  │      ├── BM25 Retrieval
  │      └── Re-ranking
  │
  └── LangChain Agent
          │
          ▼
     Structured Response
```

---

# Project Structure

```text
insurancebot/
│
├── api/
├── chains/
├── config/
├── data/
├── fallback/
├── guardrails/
├── knowledge_base/
├── memory/
├── pipelines/
├── retrieval/
├── schemas/
├── tools/
├── utils/
│
├── chatbot.py
├── main.py
├── streamlit_app.py
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# Features Implemented

## 1. AI Conversational Assistant

The chatbot supports natural language conversations related to insurance.

Example queries:

* Suggest a health insurance policy for a family
* Compare two insurance plans
* Explain waiting periods
* What is covered under a specific policy?

---

## 2. Insurance Recommendation Engine

The assistant recommends policies based on:

* Age
* Family size
* Budget
* Medical requirements
* Coverage expectations

---

## 3. Policy Comparison System

The application compares insurance policies based on:

* Premium
* Coverage
* Claim settlement ratio
* Waiting periods
* Exclusions
* Additional benefits

---

## 4. Premium Estimation

Integrated premium estimation logic provides approximate premium ranges for policies.

---

## 5. Retrieval-Augmented Generation (RAG)

The system uses RAG architecture to retrieve accurate insurance policy information.

RAG functionality includes:

* Document chunking
* Embedding generation
* Vector storage
* Semantic retrieval
* Hybrid search
* Context injection into prompts

---

## 6. Pinecone Vector Database Integration

Pinecone is used for:

* Storing vector embeddings
* Semantic similarity search
* Fast document retrieval
* Scalable vector operations

---

## 7. Hybrid Retrieval Pipeline

The retrieval pipeline combines:

* Semantic Search
* BM25 Keyword Search
* Re-ranking

This improves both accuracy and relevance.

---

## 8. Conversation Memory

The assistant maintains conversational context for follow-up questions.

Example:

User:
Compare it with Star Health.

The assistant understands the previously discussed policy.

---

## 9. Guardrails and Safety Validation

The application includes validation layers to:

* Restrict unsafe prompts
* Prevent irrelevant responses
* Filter malicious inputs
* Maintain domain-specific conversations

---

## 10. Streamlit User Interface

The frontend interface includes:

* Interactive chatbot UI
* Modern responsive design
* Session handling
* Structured response display
* Conversation reset

---

## 11. FastAPI Backend APIs

FastAPI handles:

* Chat requests
* Session management
* Health checks
* Response orchestration

---

# Retrieval-Augmented Generation (RAG) Workflow

## Step 1 — Document Loading

Insurance-related documents are loaded into the system.

## Step 2 — Text Chunking

Documents are split into smaller chunks for efficient retrieval.

## Step 3 — Embedding Generation

Embeddings are generated using OpenAI embedding models.

## Step 4 — Vector Storage

Embeddings are stored inside Pinecone.

## Step 5 — Query Embedding

User queries are converted into vector embeddings.

## Step 6 — Hybrid Retrieval

The system performs:

* Semantic vector search
* BM25 keyword retrieval
* Hybrid ranking

## Step 7 — Context Injection

Retrieved content is injected into the LLM prompt.

## Step 8 — Response Generation

The LLM generates a contextual and accurate response.

---

# Conversation Flow

```text
User Query
   │
   ▼
Frontend (Streamlit)
   │
   ▼
FastAPI Endpoint
   │
   ▼
Guardrails Validation
   │
   ▼
Query Classification
   │
   ▼
Memory Retrieval
   │
   ▼
RAG Retrieval Pipeline
   │
   ▼
LangChain Agent
   │
   ▼
LLM Response Generation
   │
   ▼
Structured Response to User
```

---

# API Endpoints

## Base Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Insurance Policy Co-Pilot Running"
}
```

---

## Chat Endpoint

```http
POST /chat
```

Sample Request:

```json
{
  "message": "Suggest a family health insurance policy"
}
```

---

## Health Check Endpoint

```http
GET /health
```

---

## Reset Conversation Endpoint

```http
POST /reset
```

---

# Installation and Setup

## Step 1 — Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Step 2— Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3 — Configure Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX=insurance-index
```

---

# Running the Application

## Start FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Start Streamlit Frontend

Open another terminal and run:

```bash
streamlit run streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# Docker Configuration

## Build Docker Image

```bash
docker build -t insurance-ai-copilot .
```

## Run Docker Container

```bash
docker run -p 8000:8000 insurance-ai-copilot
```

---

# Python Packages Used

```text
openai
langchain
langchain-openai
langchain-community
faiss-cpu
fastapi
uvicorn
streamlit
pydantic
python-dotenv
pyyaml
pytest
httpx
pinecone
langchain-pinecone
pymupdf
paddleocr
paddlepaddle
rank-bm25
sentence-transformers
tiktoken
numpy
```

---

# Testing

The project includes testing modules for:

* Document ingestion
* Retrieval pipeline
* Pinecone connectivity
* API validation
* Response handling

Testing framework used:

* Pytest

---

# Key Concepts Demonstrated

This project demonstrates implementation of:

* Generative AI Applications
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Hybrid Retrieval
* Prompt Engineering
* LangChain Agents
* AI Guardrails
* Conversational Memory
* FastAPI Backend Development
* Streamlit Frontend Development
* AI Workflow Orchestration

---

# Performance Highlights

* Modular architecture for scalability
* Hybrid retrieval for improved accuracy
* Reduced hallucinations using RAG
* Context-aware conversation handling
* Fast semantic retrieval using Pinecone
* Structured AI response generation

# Conclusion

Insurance AI Copilot is a complete AI-powered insurance assistant that combines:

* Large Language Models
* Retrieval-Augmented Generation
* Vector Databases
* Hybrid Retrieval
* Contextual Memory
* FastAPI APIs
* Streamlit User Interface
* LangChain Orchestration

The project provides a scalable, modular, and production-oriented architecture for intelligent insurance assistance systems.
