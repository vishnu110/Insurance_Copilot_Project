from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate
)

from langchain_core.example_selectors import (
    SemanticSimilarityExampleSelector
)

from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

from prompts.examples import examples


# Example prompt format
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}")
    ]
)


# Semantic selector
example_selector = (
    SemanticSimilarityExampleSelector
    .from_examples(
        examples,
        OpenAIEmbeddings(),
        FAISS,
        k=2
    )
)


# Few-shot prompt
few_shot_prompt = (
    FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        example_selector=example_selector
    )
)


# Final prompt
final_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an advanced Insurance Policy Co-Pilot.

Always return ONLY valid JSON.

Use this schema exactly:

{
  "recommendations": [],
  "coverage_gaps": [],
  "estimated_annual_premium": 0,
  "policy_comparisons": [],
  "summary": ""
}
"""
        ),

        few_shot_prompt,

        ("human", "{input}")
    ]
)