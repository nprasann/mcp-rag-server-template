from rag.loaders import load_documents_from_folder
from rag.embeddings import embed_texts
from rag.vectorstore import get_collection, index_chunks, search


def chunk_text(text: str, chunk_size: int = 200, overlap: int = 30, min_chunk_length: int = 40):
    """
    Split text into overlapping chunks and skip very small trailing fragments.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if len(chunk) >= min_chunk_length:
            chunks.append(chunk)

        start += max(1, chunk_size - overlap)

    return chunks


def ensure_index_exists(data_folder="data", collection_name="mcp_rag_demo"):
    """
    Build the vector index only if it does not already exist.
    """
    documents = load_documents_from_folder(data_folder)
    collection = get_collection(collection_name)

    if collection.count() == 0:
        all_chunks = []
        all_metadatas = []

        for doc in documents:
            chunks = chunk_text(doc["content"])
            for chunk in chunks:
                all_chunks.append(chunk)
                all_metadatas.append({"source": doc["filename"]})

        if all_chunks:
            chunk_embeddings = embed_texts(all_chunks)
            index_chunks(collection, all_chunks, chunk_embeddings, all_metadatas)

    return collection


def search_documents(question: str, top_k: int = 3):
    """
    Search indexed documents and return matching source files and chunks.
    """
    collection = ensure_index_exists()
    query_embedding = embed_texts([question])[0]
    results = search(collection, query_embedding, top_k=top_k)

    retrieved_docs = results.get("documents", [])
    retrieved_meta = results.get("metadatas", [])

    retrieved_chunks = retrieved_docs[0] if retrieved_docs else []
    retrieved_metadatas = retrieved_meta[0] if retrieved_meta else []

    sources = []
    for metadata in retrieved_metadatas:
        source = metadata["source"]
        if source not in sources:
            sources.append(source)

    return {
        "question": question,
        "sources": sources,
        "chunks": retrieved_chunks
    }
def retrieve_chunks(question: str, top_k: int = 3):
    """
    Retrieve structured chunks for a given question.
    """
    collection = ensure_index_exists()
    query_embedding = embed_texts([question])[0]
    results = search(collection, query_embedding, top_k=top_k)

    retrieved_docs = results.get("documents", [])
    retrieved_meta = results.get("metadatas", [])

    retrieved_chunks = retrieved_docs[0] if retrieved_docs else []
    retrieved_metadatas = retrieved_meta[0] if retrieved_meta else []

    structured_results = []

    for i, (chunk, metadata) in enumerate(zip(retrieved_chunks, retrieved_metadatas), start=1):
        structured_results.append({
            "source": metadata["source"],
            "chunk": chunk,
            "rank": i
        })

    return {
        "question": question,
        "results": structured_results
    }