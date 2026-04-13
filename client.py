import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    # Define how to launch the MCP server process
    server_params = StdioServerParameters(
        command="python",
        args=["main.py"],
    )

    # Start the MCP server as a subprocess and connect over stdio
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the MCP session
            await session.initialize()

            print("\nConnected to MCP server\n")

            # -----------------------------
            # 1. List available tools
            # -----------------------------
            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"- {tool.name}")

            # -----------------------------
            # 2. Call list_sources_tool
            # -----------------------------
            print("\nCalling list_sources_tool...\n")
            result = await session.call_tool("list_sources_tool", {})
            print(result)

            # -----------------------------
            # 3. Call retrieve_chunks_tool
            # -----------------------------
            print("\nCalling retrieve_chunks_tool...\n")
            result = await session.call_tool(
                "retrieve_chunks_tool",
                {
                    "question": "What are the steps in RAG?",
                    "top_k": 3,
                },
            )
            print(result)


if __name__ == "__main__":
    asyncio.run(main())