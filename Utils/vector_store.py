import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="candidates")
job_collection=client.get_or_create_collection(name="job_embeddings")

def store_embedding(user_id, embedding, text):
    collection.upsert(
        ids=[user_id],
        embeddings=[embedding],
        documents=[text]
    )

def store_job_embedding(job_id,embedding,text):
    job_collection.upsert(
        ids=[job_id],
        embeddings=[embedding],
        documents=[text]
    )

def search_candidates(query_embedding, k=1):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results["ids"][0]