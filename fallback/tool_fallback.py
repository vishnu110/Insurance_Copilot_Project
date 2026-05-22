def safe_tool_execution(tool_func, *args, **kwargs):

    try:

        return tool_func(*args, **kwargs)

    except Exception as e:

        print(f"Tool execution failed: {e}")

        return {
            "tool_error": True,
            "message": (
                "Unable to process this tool request right now."
            )
        }