import json

from langchain_core.tools import tool


@tool
def policy_ranking_tool(policy_type: str):
    """
    Rank insurance policies intelligently.
    """

    with open("data/policies.json", "r") as file:
        policies = json.load(file)

    filtered = [
        p for p in policies
        if p["type"] == policy_type
    ]

    ranked = []

    for policy in filtered:

        score = 0

        # Higher CSR better
        score += policy["claim_settlement_ratio"]

        # Lower premium better
        score += max(0, 25000 - policy["premium"]) / 1000

        # No copay preferred
        if not policy["co_pay"]:
            score += 10

        # Lower waiting period
        score += max(0, 30 - policy["waiting_period"])

        ranked.append(
            {
                "name": policy["name"],
                "score": round(score, 2),
                "premium": policy["premium"],
                "claim_ratio":
                    policy["claim_settlement_ratio"]
            }
        )

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked