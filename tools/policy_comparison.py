# tools/policy_comparison.py

import json
from pathlib import Path
from langchain_core.tools import tool

@tool
def policy_comparison_tool(policy_type: str) -> list | str:
    """Compare insurance policies based on type (e.g., 'health', 'term').

    Args:
        policy_type: The type of insurance policy to compare.
    """

    # Robust path resolution — works regardless of working directory
    data_path = Path(__file__).parent.parent / "data" / "policies.json"

    with open(data_path, "r") as file:
        policies = json.load(file)

    filtered = [p for p in policies if p["type"] == policy_type]

    if not filtered:
        return f"No matching policies found for type: '{policy_type}'"

    result = [
        {
            "name": policy["name"],
            "premium": policy["premium"],
            "claim_ratio": policy["claim_settlement_ratio"],
            "coverage": policy["coverage"],
        }
        for policy in filtered
    ]

    return result