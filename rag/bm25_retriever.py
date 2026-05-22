import json

from rank_bm25 import BM25Okapi


# =========================
# LOAD KNOWLEDGE
# =========================

with open(
    "data/insurance_knowledge.json",
    "r"
) as f:

    documents = json.load(f)


# =========================
# TOKENIZE
# =========================

corpus = [

    doc["content"].lower().split()

    for doc in documents
]


bm25 = BM25Okapi(corpus)


# =========================
# BM25 SEARCH
# =========================

def bm25_search(
    query,
    top_k=3
):

    tokenized_query = query.lower().split()

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked_docs = sorted(

        zip(documents, scores),

        key=lambda x: x[1],

        reverse=True
    )

    results = []

    for doc, score in ranked_docs[:top_k]:

        results.append({

            "text":
                doc["content"],

            "score":
                float(score)
        })

    return results