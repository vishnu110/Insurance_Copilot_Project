import json

from rag.pinecone_client import index
from rag.knowledge_base import create_vector_record


def ingest_documents(documents):

    vectors = []

    for i, doc in enumerate(documents):

        vector_record = create_vector_record(

            doc_id=f"chunk_{i}",

            text=doc
        )

        vectors.append(vector_record)

    index.upsert(vectors=vectors)

    print(f"Inserted {len(vectors)} chunks.")