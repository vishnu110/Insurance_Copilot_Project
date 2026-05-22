def default_response(summary, response_type="general"):

    return {

        "response_type": response_type,

        "recommendations": [],

        "coverage_gaps": [],

        "premium_details": {},

        "policy_comparisons": [],

        "summary": summary
    }