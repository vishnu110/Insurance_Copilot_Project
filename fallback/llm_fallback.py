from openai import RateLimitError


def handle_llm_error(error):

    error_message = str(error).lower()

    if "rate limit" in error_message:

        return (
            "The AI service is currently busy. "
            "Please try again in a few moments."
        )

    elif "timeout" in error_message:

        return (
            "The request took too long to process. "
            "Please try again."
        )

    elif "connection" in error_message:

        return (
            "Unable to connect to the AI service right now."
        )

    return (
        "I'm temporarily unable to process your request."
    )