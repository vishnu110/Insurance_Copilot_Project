DOCUMENT_KEYWORDS = [

    "policy",
    "document",
    "coverage",
    "waiting period",
    "exclusion",
    "claim",
    "cataract",
    "ambulance",
    "sum insured",
    "premium",
    "day care",
    "hospitalization"
]


def is_document_query(query):

    query = query.lower()

    return any(

        keyword in query

        for keyword in DOCUMENT_KEYWORDS
    )