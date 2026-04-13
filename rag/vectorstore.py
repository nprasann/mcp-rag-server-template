import chromadb


def get_collection(name="mcp_rag_demo", persist_directory="chroma_db"):
    """
    Create or open a persistent ChromaDB collection.
    """
    client = chromadb.PersistentClient(path=persist_directory)
    return client.get_or_create_collection(name=name)


def index_chunks(collection, chunks, embeddings, metadatas):
    """
    Store chunks, embeddings, and metadata in the vector store.
    """
    ids = [f"chunk-{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search(collection, query_embedding, top_k=3):
    """
    Search the collection using a query embedding.
    """
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )