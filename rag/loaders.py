from pathlib import Path


def load_text_file(path: str) -> str:
    """
    Load a plain text or markdown file and return its contents.
    """
    return Path(path).read_text(encoding="utf-8")


def load_documents_from_folder(folder_path: str):
    """
    Load supported files from a folder.

    Supported types:
    - .txt
    - .md

    Returns:
        A list of dicts like:
        {
            "filename": "...",
            "content": "..."
        }
    """
    folder = Path(folder_path)
    documents = []

    for file_path in folder.glob("*.txt"):
        documents.append({
            "filename": file_path.name,
            "content": load_text_file(str(file_path))
        })

    for file_path in folder.glob("*.md"):
        documents.append({
            "filename": file_path.name,
            "content": load_text_file(str(file_path))
        })

    return documents