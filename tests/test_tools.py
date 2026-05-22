from tools.premium_estimator import (
    premium_estimator_tool
)

from tools.needs_assessment import (
    needs_assessment_tool
)

from tools.policy_ranking import (
    policy_ranking_tool
)


def test_premium_estimator():

    result = premium_estimator_tool.invoke(
        {
            "age": 45,
            "coverage_amount": 10000000,
            "smoker": True,
            "health_condition": "diabetic"
        }
    )

    assert result["yearly_premium"] > 0

    assert result["monthly_premium"] > 0


def test_needs_assessment():

    result = needs_assessment_tool.invoke(
        {
            "age": 32,
            "income": 1800000,
            "dependents": 1,
            "health_condition": "diabetic",
            "marital_status": "married"
        }
    )

    assert (
        "Term Life Insurance"
        in result["recommended_policies"]
    )


def test_policy_ranking():

    result = policy_ranking_tool.invoke(
        {
            "policy_type": "health"
        }
    )

    assert len(result) > 0

    assert "score" in result[0]