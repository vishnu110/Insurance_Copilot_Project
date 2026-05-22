examples = [

    {
        "input":
            "I am 32 married with one child earning 18L",

        "output":
        """
{
  "recommendations": [
    "Term Life Insurance",
    "Family Health Insurance",
    "Critical Illness Rider"
  ],

  "coverage_gaps": [
    "No existing insurance coverage"
  ],

  "estimated_annual_premium": 35000,

  "policy_comparisons": [],

  "summary":
    "A family protection strategy including life and health insurance is recommended."
}
"""
    },

    {
        "input":
            "Suggest insurance for diabetic patient",

        "output":
        """
{
  "recommendations": [
    "Diabetes-friendly Health Insurance",
    "Term Life Insurance"
  ],

  "coverage_gaps": [
    "No existing insurance coverage"
  ],

  "estimated_annual_premium": 28000,

  "policy_comparisons": [],

  "summary":
    "Health insurance with diabetes coverage is highly recommended."
}
"""
    },

    {
        "input":
            "Compare health insurance policies",

        "output":
        """
{
  "recommendations": [
    "HDFC Ergo Optima Secure",
    "Niva Bupa ReAssure"
  ],

  "coverage_gaps": [],

  "estimated_annual_premium": 0,

  "policy_comparisons": [
    {
      "name": "HDFC Ergo Optima Secure",
      "premium": 16800,
      "claim_ratio": 95,
      "coverage": 1000000
    },

    {
      "name": "Niva Bupa ReAssure",
      "premium": 21000,
      "claim_ratio": 91,
      "coverage": 1500000
    }
  ],

  "summary":
    "HDFC Ergo provides affordability while Niva Bupa offers higher coverage."
}
"""
    },

    {
        "input":
            "Estimate premium for 1Cr coverage age 45 smoker diabetic",

        "output":
        """
{
  "recommendations": [],

  "coverage_gaps": [],

  "estimated_annual_premium": 21840,

  "policy_comparisons": [],

  "summary":
    "Estimated premium for the requested profile is approximately ₹21,840 annually."
}
"""
    }

]