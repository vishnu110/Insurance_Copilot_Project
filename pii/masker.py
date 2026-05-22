import re

from pii.detector import (
    PII_PATTERNS
)


# =========================================
# MASK PII
# =========================================

def mask_pii(text):

    masked_text = text

    for pii_type, pattern in PII_PATTERNS.items():

        masked_text = re.sub(

            pattern,

            f"[REDACTED_{pii_type.upper()}]",

            masked_text
        )

    return masked_text