import os

from ocr.pdf_extractor import (
    extract_pdf_text
)

from ocr.vision_ocr import (
    extract_text_from_image
)

from pii.sanitizer import (
    sanitize_text
)

from ocr.cleaner import clean_text

from ocr.chunker import chunk_text

from rag.ingest import ingest_documents


def ingest_document(file_path):

    # =========================
    # FILE EXTENSION
    # =========================

    extension = os.path.splitext(
        file_path
    )[1].lower()

    # =========================
    # PDF EXTRACTION
    # =========================

    if extension == ".pdf":

        raw_text = extract_pdf_text(
            file_path
        )

    # =========================
    # IMAGE OCR
    # =========================

    elif extension in [
        ".png",
        ".jpg",
        ".jpeg",
        ".webp"
    ]:

        raw_text = extract_text_from_image(
            file_path
        )

    else:

        raise ValueError(
            f"Unsupported file format: {extension}"
        )

    # =========================
    # CLEAN TEXT
    # =========================

    cleaned_text = clean_text(
            raw_text
        )

    # =========================================
    # PII SANITIZATION
    # =========================================

    sanitized_result = sanitize_text(
        cleaned_text
    )

    cleaned_text = sanitized_result[
        "sanitized_text"
    ]

    print(
        "\nDETECTED PII:\n"
    )

    print(
        sanitized_result[
            "detected_pii"
        ]
    )

    # =========================
    # CHUNKING
    # =========================

    chunks = chunk_text(
        cleaned_text
    )

    # =========================
    # INGEST INTO PINECONE
    # =========================

    ingest_documents(
        chunks
    )

    return {

        "chunks_ingested":
            len(chunks)
    }