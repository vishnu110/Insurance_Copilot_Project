from langchain_openai import ChatOpenAI

from rag.context_builder import (
    build_rag_context
)


llm = ChatOpenAI(

    model="gpt-4.1-mini",

    temperature=0
)


def answer_document_query(query):

    context = build_rag_context(
        query
    )

    prompt = f"""

You are an insurance document analyst.

Answer ONLY using the retrieved policy information.

If information is unavailable,
say:

"The uploaded policy document does not clearly specify this."

Question:
{query}

{context}

Provide a concise factual answer.

"""

    response = llm.invoke(
        prompt
    )

    return response.content