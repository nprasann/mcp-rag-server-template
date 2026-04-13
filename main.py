from server.tools import TOOLS
from server.handlers import list_sources


def main():
    print("Available tools:")
    for tool in TOOLS:
        print(f"- {tool['name']}: {tool['description']}")

    print("\nTesting list_sources...\n")
    result = list_sources()
    print(result)


if __name__ == "__main__":
    main()