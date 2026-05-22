from rag.ingest import ingest_json_knowledge
from rag.retriever import retrieve_context


# =========================
# INGEST DATA
# =========================

ingest_json_knowledge(
    "data/insurance_knowledge.json"
)

# =========================
# TEST RETRIEVAL
# =========================

query = "Why are smokers charged higher premiums?"

result = retrieve_context(query)

print("\nRETRIEVED CONTEXT:\n")

print(result)