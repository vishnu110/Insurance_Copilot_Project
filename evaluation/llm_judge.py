import json

from fallback.llm_fallback import (
    invoke_llm_with_fallback
)

from evaluation.judge_prompt import (
    JUDGE_PROMPT
)


# =========================================
# MAIN JUDGE FUNCTION
# =========================================

def evaluate_response(

    user_query,
    assistant_response
):

    prompt = f"""

{JUDGE_PROMPT}

USER QUERY:
{user_query}

ASSISTANT RESPONSE:
{assistant_response}

"""

    try:

        result = invoke_llm_with_fallback(
            prompt
        )

        response_text = result.content

        parsed = json.loads(
            response_text
        )

        return parsed

    except Exception as e:

        print(
            f"Judge evaluation error: {e}"
        )

        return {

            "relevance_score": 0,

            "groundedness_score": 0,

            "hallucination_risk": 0,

            "completeness_score": 0,

            "hallucination_detected": True,

            "short_feedback":
                "Evaluation failed."
        }