# End-to-End Medical Chatbot using Llama 2 (70B)

## 🧠 Overview

This project is an AI-powered Medical Chatbot built using Llama 2 (70B), designed to provide intelligent responses to medical-related queries.
It demonstrates how to integrate LLMs, LangChain, Vector Databases (Pinecone), and Flask to build an end-to-end conversational medical assistant.

## Requirements / Prerequisites

1. Python 3.10+

2. Access to Llama 2 70B weights (local or hosted service) — ensure licensing and hardware capability.

3. GPU(s) with sufficient VRAM and system memory OR an API endpoint that serves Llama 2 70B.

4. Vector DB account or local install (Pinecone, FAISS, Milvus, Chroma, etc.)

5. Recommended libraries: transformers / accelerate (or vendor SDK), sentence-transformers (or model for embeddings), faiss / pinecone-client, flask or fastapi, uvicorn, langchain (optional helper), pdfplumber or PyMuPDF for PDF extraction.

6. Docker (optional) for containerized deployment.

## Ethical & Safety Notes (Read Carefully)

1. This chatbot is for research and educational use. It is not medical advice.

2. Include visible disclaimers in the UI: always consult a licensed medical professional.

3. Implement rate limits, logging, and human-in-the-loop escalation for high-risk answers.

4. Use trusted, curated medical sources for the retrieval corpus (peer-reviewed docs, clinical guidelines).

5. Keep a record of document sources and expose citations to users.