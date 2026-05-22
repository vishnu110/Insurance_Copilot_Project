from langchain_core.tools import tool


@tool
def premium_estimator_tool(
    age: int,
    coverage_amount: int,
    smoker: bool = False,
    tenure: int = 30,
    health_condition: str = ""
):
    """
    Intelligent insurance premium estimator.
    """

    try:

        # =========================
        # INPUT VALIDATION
        # =========================

        if age <= 0 or age > 100:

            return {
                "tool_error": True,
                "message": (
                    "Please provide a valid age "
                    "between 1 and 100."
                )
            }

        if coverage_amount <= 0:

            return {
                "tool_error": True,
                "message": (
                    "Coverage amount must be greater than zero."
                )
            }

        if tenure <= 0:

            return {
                "tool_error": True,
                "message": (
                    "Tenure must be greater than zero."
                )
            }

        # =========================
        # BASE PREMIUM
        # =========================

        premium = coverage_amount * 0.0008

        # =========================
        # AGE LOADING
        # =========================

        if age >= 60:

            premium *= 2.5

        elif age > 50:

            premium *= 2

        elif age > 40:

            premium *= 1.5

        elif age > 30:

            premium *= 1.2

        # =========================
        # SMOKER LOADING
        # =========================

        if smoker:

            premium *= 1.4

        # =========================
        # HEALTH CONDITIONS
        # =========================

        condition = health_condition.lower()

        serious_conditions = [
            "cancer",
            "kidney",
            "heart",
            "cardiac",
            "stroke"
        ]

        # Diabetes

        if "diabetic" in condition:

            premium *= 1.3

        # Serious illnesses

        if any(
            cond in condition
            for cond in serious_conditions
        ):

            premium *= 1.6

        # Hypertension / Asthma

        if (
            "hypertension" in condition
            or "asthma" in condition
        ):

            premium *= 1.15

        # =========================
        # TENURE LOADING
        # =========================

        if tenure > 30:

            premium *= 1.2

        # =========================
        # FINAL PREMIUMS
        # =========================

        yearly_premium = round(premium)

        monthly_premium = round(
            yearly_premium / 12,
            2
        )

        # =========================
        # RETURN
        # =========================

        return {

            "tool_error": False,

            "coverage_amount":
                coverage_amount,

            "age":
                age,

            "smoker":
                smoker,

            "health_condition":
                health_condition,

            "tenure":
                tenure,

            "yearly_premium":
                yearly_premium,

            "monthly_premium":
                monthly_premium
        }

    except Exception as e:

        print(f"Premium tool error: {e}")

        return {

            "tool_error": True,

            "message": (
                "Unable to estimate premium right now."
            )
        }