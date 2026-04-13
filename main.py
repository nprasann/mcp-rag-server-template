from dotenv import load_dotenv
from server.tools import TOOLS
from server.handlers import list_sources, search_documents


def main():
    load_dotenv()

    print("Available tools:")
    for tool in TOOLS:
        print(f"- {tool['name']}: {tool['description']}")

    print("\nTesting list_sources...\n")
    print(list_sources())

    print("\nTesting search_documents...\n")
    result = search_documents("What are the common steps in RAG?", top_k=3)
    print(result)


if __name__ == "__main__":
    main()