import re


def clean_text(text):

    # remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()