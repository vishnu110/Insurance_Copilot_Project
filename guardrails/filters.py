from langchain_openai import ChatOpenAI


# =====================================
# VALIDATOR MODEL
# =====================================

validator_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=20
)


# =====================================
# GUARDRAIL FUNCTION
# =====================================

def run_guardrails(user_input: str):

    prompt = f"""
Classify the following user query into ONE category only.

Categories:

GREETING
INSURANCE
FOLLOW_UP
FICTIONAL
OUT_OF_SCOPE
UNREALISTIC

Rules:

- GREETING:
  hi, hello, hey, thanks, okay

- INSURANCE:
  realistic insurance-related requests

- FOLLOW_UP:
  short contextual replies like:
  "health"
  "yes"
  "compare"
  "for parents"

- FICTIONAL:
  superheroes, fictional entities

- OUT_OF_SCOPE:
  weather, sports, movies, coding

- UNREALISTIC:
  superpowers, magic abilities, impossible situations

Respond ONLY with ONE WORD.

Query:
{user_input}
"""

    try:

        category = validator_llm.invoke(
            prompt
        ).content.strip().upper()

        # =====================================
        # GREETING
        # =====================================

        if category == "GREETING":

            return {
                "blocked": False
            }

        # =====================================
        # INSURANCE
        # =====================================

        if category == "INSURANCE":

            return {
                "blocked": False
            }

        # =====================================
        # FOLLOW UP
        # =====================================

        if category == "FOLLOW_UP":

            return {
                "blocked": False
            }

        # =====================================
        # FICTIONAL
        # =====================================

        if category == "FICTIONAL":

            return {

                "blocked": True,

                "response":
                    "I can provide insurance guidance only for real individuals and real-world scenarios."
            }

        # =====================================
        # UNREALISTIC
        # =====================================

        if category == "UNREALISTIC":

            return {

                "blocked": True,

                "response":
                    "I can only assist with realistic insurance-related situations."
            }

        # =====================================
        # OUT OF SCOPE
        # =====================================

        if category == "OUT_OF_SCOPE":

            return {

                "blocked": True,

                "response":
                    "I specialize only in insurance-related assistance."
            }

        # =====================================
        # DEFAULT ALLOW
        # =====================================

        return {
            "blocked": False
        }

    except Exception:

        return {
            "blocked": False
        }