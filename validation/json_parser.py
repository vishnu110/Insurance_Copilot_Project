import json
import re


def extract_json(text: str):

    try:

        return json.loads(text)

    except Exception:

        pass

    # =========================
    # TRY EXTRACTING JSON BLOCK
    # =========================

    try:

        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL
        )

        if match:

            json_text = match.group()

            return json.loads(json_text)

    except Exception:

        pass

    return None