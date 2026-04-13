# mcp-rag-server-template

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-v1--complete-success)
![MCP](https://img.shields.io/badge/MCP-server-purple)
![RAG](https://img.shields.io/badge/AI-RAG-orange)

A starter **MCP server template** that exposes **RAG-style retrieval tools** using Python.  
This project demonstrates how to connect document retrieval capabilities to an MCP-compatible client through a clean, language-agnostic architecture.

---

## 🚀 Features

### MCP Server Capabilities
- MCP server runtime using Python
- Tool registration through FastMCP
- Local MCP client for testing tool calls
- Structured tool outputs suitable for downstream LLM use

### Retrieval / RAG Capabilities
- Document loading from local files
- Text chunking
- Embedding generation using OpenAI
- Persistent vector storage with ChromaDB
- Retrieval of relevant chunks for a question
- Source tracking in results

### Tooling
- `list_sources_tool`
- `search_documents_tool`
- `retrieve_chunks_tool`

---

## 🧠 Architecture

This repo separates concerns into layers:

- MCP layer → tool registration and runtime
- Handler layer → tool implementations
- RAG layer → document loading, chunking, embeddings, vector search
- Client layer → local test harness

Flow:
User → MCP Client → MCP Server → Tools → RAG Layer → OpenAI + ChromaDB → Structured Results

---

## 🛠️ Exposed Tools

- list_sources_tool
- search_documents_tool
- retrieve_chunks_tool

---

## 📂 Project Structure

main.py  
client.py  

server/  
rag/  
data/  
outputs/  

---

## ⚡ Setup

pip install -r requirements.txt

Create .env:
OPENAI_API_KEY=your_openai_api_key_here

---

## ▶️ Run Server

python main.py

---

## 🧪 Test Client

python client.py

---

## ⭐

Star, fork, and extend this MCP-based retrieval service.
