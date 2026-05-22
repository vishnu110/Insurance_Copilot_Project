# utils/response_parser.py

import json
from schemas.models import InsuranceResponse

def parse_insurance_response(response) -> dict:
    """
    Accepts:
      - dict  (already parsed by chatbot._parse_llm_output)
      - str   (plain conversational reply)
    """
    try:
        # If still a string here, treat as plain summary
        if isinstance(response, str):
            return InsuranceResponse(
                response_type="general",
                summary=response
            ).model_dump()

        parsed = response  # already a dict

        # Unwrap nested keys if LLM wraps output
        for wrapper_key in ("recommendation", "result", "response", "data"):
            if wrapper_key in parsed and isinstance(parsed[wrapper_key], dict):
                parsed = parsed[wrapper_key]
                break

        # Detect response type
        response_type = "general"
        if "premium_estimate" in parsed or "estimated_annual_premium" in parsed:
            response_type = "premium_estimation"
        elif any(k in parsed for k in (
            "recommended_policy_types", "recommendations",
            "recommended_policies", "insurance_types"
        )):
            response_type = "recommendation"
        elif "health_insurance_policy_comparison" in parsed:
            response_type = "comparison"

        # Recommendations
        recommendations = []
        if "recommended_policy_types" in parsed:
            recommendations = parsed.get("recommended_policy_types", [])
        elif "recommended_policies" in parsed:
            for p in parsed.get("recommended_policies", []):
                if isinstance(p, dict):
                    recommendations.append(p.get("type", str(p)))
                else:
                    recommendations.append(str(p))
        elif "recommendations" in parsed:
            rec = parsed["recommendations"]
            if isinstance(rec, list):
                recommendations = rec
            elif isinstance(rec, dict):
                recommendations = rec.get("insurance_types", [])

        # Coverage gaps
        coverage_gaps = []
        gap = parsed.get("coverage_gap")
        if gap:
            coverage_gaps = gap if isinstance(gap, list) else [gap]

        # Premium details
        premium_details = {}
        if "premium_estimate" in parsed:
            premium_details = parsed["premium_estimate"]
        elif "estimated_annual_premium" in parsed or "yearly_premium" in parsed:
            premium_details = {
                k: parsed[k] for k in (
                    "estimated_annual_premium", "yearly_premium", "monthly_premium"
                ) if k in parsed
            }

        # Policy comparisons
        policy_comparisons = parsed.get(
            "health_insurance_policy_comparison",
            parsed.get("policy_comparisons", [])
        )

        # Summary
        summary = parsed.get("summary", parsed.get("recommendation_summary", ""))

        # If nothing useful extracted, fall back to whole dict as summary
        if not summary and not recommendations and not coverage_gaps and not premium_details:
            summary = json.dumps(parsed)

        return InsuranceResponse(
            response_type=response_type,
            recommendations=recommendations,
            coverage_gaps=coverage_gaps,
            premium_details=premium_details,
            policy_comparisons=policy_comparisons,
            summary=summary
        ).model_dump()

    except Exception as e:
        print(f"Parser error: {e}")
        return InsuranceResponse(
            response_type="raw",
            summary=str(response)
        ).model_dump()