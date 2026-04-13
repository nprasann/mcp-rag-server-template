# mcp-rag-server-template

A starter MCP server template that exposes RAG-style retrieval tools using Python.

## Initial Goals
- expose retrieval as MCP tools
- keep MCP server logic separate from RAG logic
- support future portability to Node, C#, or Java

## Planned Tools
- `list_sources`
- `search_documents`
- `retrieve_chunks`