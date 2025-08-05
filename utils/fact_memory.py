import chromadb
from sentence_transformers import SentenceTransformer
from typing import List, Dict
import chromadb
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

client = chromadb.PersistentClient(path="./chroma_storage")
collection = client.get_or_create_collection("validated_facts")

# Embedding model for vector search
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def store_fact(fact_text: str, metadata: Dict):
    embedding = embedder.encode(fact_text).tolist()
    collection.add(
        documents=[fact_text],
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[metadata.get("id") or fact_text[:32]]
    )

def query_facts(query_text: str, top_k: int = 5) -> List[Dict]:
    embedding = embedder.encode(query_text).tolist()
    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    # Safety check to avoid TypeError if no results
    if (
        not results
        or not results.get("documents")
        or results.get("documents") is None
        or not results["documents"]
        or not results["documents"][0]
    ):
        return []

    # Additional safety check for 'distances' and 'metadatas'
    if (
        not results.get("distances")
        or results["distances"] is None
        or not results["distances"][0]
        or not results.get("metadatas")
        or results["metadatas"] is None
        or not results["metadatas"][0]
    ):
        return []

    return [
        {
            "fact": doc,
            "score": score,
            "metadata": meta
        }
        for doc, score, meta in zip(
            results["documents"][0],
            results["distances"][0],
            results["metadatas"][0]
        )
    ]

def reset_memory():
    collection.delete()
    client.reset()
