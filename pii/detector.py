import re


# =========================================
# PII REGEX PATTERNS
# =========================================

PII_PATTERNS = {

    "email":

        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",

    "phone":

        r"\b\d{10}\b",

    "aadhaar":

        r"\b\d{4}\s?\d{4}\s?\d{4}\b",

    "pan":

        r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b",

    "credit_card":

        r"\b(?:\d[ -]*?){13,16}\b"
}


# =========================================
# DETECT PII
# =========================================

def detect_pii(text):

    detected = {}

    for pii_type, pattern in PII_PATTERNS.items():

        matches = re.findall(
            pattern,
            text
        )

        if matches:

            detected[pii_type] = matches

    return detected