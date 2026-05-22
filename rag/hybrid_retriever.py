from rag.retriever import retrieve_context
from rag.bm25_retriever import bm25_search


def hybrid_retrieve(
    query
):

    # =========================
    # DENSE SEARCH
    # =========================

    dense_results = retrieve_context(
        query
    )

    dense_chunks = [

        chunk.strip()

        for chunk in dense_results.split("\n\n")

        if chunk.strip()
    ]

    # =========================
    # BM25 SEARCH
    # =========================

    sparse_results = bm25_search(
        query
    )

    sparse_chunks = [

        item["text"]

        for item in sparse_results
    ]

    # =========================
    # MERGE RESULTS
    # =========================

    combined = list(

        dict.fromkeys(

            dense_chunks +
            sparse_chunks
        )
    )

    return combined