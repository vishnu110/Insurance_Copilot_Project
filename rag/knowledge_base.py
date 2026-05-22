from rag.embeddings import embeddings


def create_vector_record(
    doc_id,
    text,
    metadata=None
):

    vector = embeddings.embed_query(text)

    return {

        "id": str(doc_id),

        "values": vector,

        "metadata": {

            "text": text,

            **(metadata or {})
        }
    }