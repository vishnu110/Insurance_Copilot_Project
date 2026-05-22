def rerank_results(
    query,
    documents,
    top_k=8
):

    query_words = set(
        query.lower().split()
    )

    scored = []

    for doc in documents:

        doc_words = set(
            doc.lower().split()
        )

        overlap = len(
            query_words.intersection(
                doc_words
            )
        )

        scored.append(
            (doc, overlap)
        )

    ranked = sorted(

        scored,

        key=lambda x: x[1],

        reverse=True
    )

    return [

        item[0]

        for item in ranked[:top_k]
    ]