from ocr.ingestion_pipeline import (
    ingest_document
)

result = ingest_document(
    "Insurance_FAQs.pdf"
)

print(result)