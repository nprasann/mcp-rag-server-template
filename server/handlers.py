from pathlib import Path


def list_sources(data_folder="data"):
    """
    Return a sorted list of supported source files in the data folder.
    """
    folder = Path(data_folder)

    supported_extensions = {".txt", ".md", ".pdf"}
    files = [
        file_path.name
        for file_path in folder.iterdir()
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions
    ]

    return {
        "sources": sorted(files),
        "count": len(files)
    }