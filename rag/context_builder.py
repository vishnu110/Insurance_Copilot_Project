from rag.hybrid_retriever import hybrid_retrieve
from rag.reranker import rerank_results


def build_rag_context(user_query):

    retrieved_docs = hybrid_retrieve(
        user_query
    )

    top_docs = rerank_results(

        query=user_query,

        documents=retrieved_docs,

        top_k=5
    )

    if not top_docs:

        return ""

    context = "\n\n".join(
        top_docs
    )

    return f"""

IMPORTANT INSTRUCTIONS:

Answer ONLY using the retrieved insurance policy information below.

If the answer is not present in the retrieved context,
say:

"The uploaded policy document does not clearly specify this information."

Do NOT use general insurance knowledge.
Do NOT make assumptions.
Do NOT hallucinate.

Retrieved Policy Information:

{context}

"""