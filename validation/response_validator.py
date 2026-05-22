from schemas.models import InsuranceResponse


def validate_response(data):

    try:

        validated = InsuranceResponse(
            **data
        )

        return validated.model_dump()

    except Exception as e:

        print(f"Validation error: {e}")

        return None