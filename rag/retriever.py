from rag.embeddings import embeddings
from rag.pinecone_client import index


def retrieve_context(
    query,
    top_k=3
):

    query_vector = embeddings.embed_query(
        query
    )

    results = index.query(

        vector=query_vector,

        top_k=top_k,

        include_metadata=True
    )

    matches = results.get(
        "matches",
        []
    )

    contexts = []

    for match in matches:

        metadata = match.get(
            "metadata",
            {}
        )

        text = metadata.get(
            "text",
            ""
        )

        contexts.append(text)

    return "\n\n".join(contexts)