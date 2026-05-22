from typing import Optional
from langchain_core.tools import tool


@tool
def needs_assessment_tool(
    age: Optional[int] = None,
    income: Optional[int] = None,
    dependents: Optional[int] = None,
    existing_cover: str = "None",
    health_condition: str = "",
    marital_status: str = "single"
):
    """
    Intelligent insurance needs assessment.
    """

    recommendations = []
    gaps = []

    condition = health_condition.lower()

    # =========================
    # HEALTH CONDITIONS
    # =========================

    if "diabetic" in condition:

        recommendations.append(
            "Diabetes-friendly Health Insurance"
        )

    if (
        "cancer" in condition
        or "heart" in condition
        or "cardiac" in condition
        or "kidney" in condition
    ):

        recommendations.append(
            "Critical Illness Insurance"
        )

        recommendations.append(
            "Comprehensive Health Insurance"
        )

    # =========================
    # FAMILY SIZE
    # =========================

    if dependents and dependents >= 2:

        recommendations.append(
            "Family Health Insurance"
        )

    if dependents and dependents >= 10:

        recommendations.append(
            "Group Insurance Plan"
        )

    # =========================
    # LIFE INSURANCE
    # =========================

    if age and age < 50:

        recommendations.append(
            "Term Life Insurance"
        )

    # =========================
    # HIGH INCOME
    # =========================

    if income and income > 1500000:

        recommendations.append(
            "Critical Illness Rider"
        )

    # =========================
    # MARRIED USERS
    # =========================

    if marital_status.lower() == "married":

        recommendations.append(
            "Family Protection Plan"
        )

    # =========================
    # COVERAGE GAPS
    # =========================

    if existing_cover.lower() == "none":

        gaps.append(
            "No existing insurance coverage"
        )

    # =========================
    # PREMIUM ESTIMATION
    # =========================

    estimated_premium = 25000

    if "diabetic" in condition:

        estimated_premium += 10000

    if (
        "cancer" in condition
        or "heart" in condition
    ):

        estimated_premium += 30000

    if dependents:

        estimated_premium += dependents * 1000

    # =========================
    # FALLBACK
    # =========================

    if not recommendations:

        recommendations.append(
            "Health Insurance"
        )

    return {

        "recommended_policies":
            list(set(recommendations)),

        "coverage_gap":
            gaps,

        "estimated_annual_premium":
            estimated_premium,

        "recommendation_summary":
            "Insurance needs assessed successfully"
    }