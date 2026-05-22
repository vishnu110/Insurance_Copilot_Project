from evaluation.llm_judge import (
    evaluate_response
)


# =========================================
# WRAPPER
# =========================================

def run_evaluation(

    query,
    response
):

    result = evaluate_response(

        user_query=query,

        assistant_response=response
    )

    return result