from pii.detector import (
    detect_pii
)

from pii.masker import (
    mask_pii
)


# =========================================
# SANITIZE TEXT
# =========================================

def sanitize_text(text):

    detected_pii = detect_pii(
        text
    )

    sanitized_text = mask_pii(
        text
    )

    return {

        "sanitized_text":
            sanitized_text,

        "detected_pii":
            detected_pii
    }