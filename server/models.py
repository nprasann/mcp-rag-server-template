from dataclasses import dataclass
from typing import Optional


@dataclass
class ListSourcesInput:
    """
    Input model for listing available source documents.
    """
    pass


@dataclass
class SearchDocumentsInput:
    """
    Input model for searching documents by a user question.
    """
    question: str
    top_k: int = 3
    source_filter: Optional[str] = None


@dataclass
class RetrieveChunksInput:
    """
    Input model for retrieving chunks for a given question.
    """
    question: str
    top_k: int = 3
    source_filter: Optional[str] = None