from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from server.handlers import list_sources, search_documents, retrieve_chunks

# Load environment variables
load_dotenv()

# Create MCP server
mcp = FastMCP("mcp-rag-server-template")


@mcp.tool()
def list_sources_tool() -> dict:
    """
    List all supported source files in the data folder.
    """
    return list_sources()


@mcp.tool()
def search_documents_tool(question: str, top_k: int = 3) -> dict:
    """
    Search indexed documents using a user question and return matching sources/chunks.
    """
    return search_documents(question=question, top_k=top_k)


@mcp.tool()
def retrieve_chunks_tool(question: str, top_k: int = 3) -> dict:
    """
    Retrieve structured chunks for a user question.
    """
    return retrieve_chunks(question=question, top_k=top_k)


if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run()