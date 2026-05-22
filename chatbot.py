import uuid
import json

from chains.insurance_chain import insurance_agent

from utils.logger import log_interaction

from guardrails.filters import run_guardrails

from fallback.llm_fallback import handle_llm_error
from fallback.response_formatter import default_response
from validation.json_parser import extract_json
from validation.response_validator import validate_response
from rag.context_builder import build_rag_context
from rag.query_router import (
    is_document_query
)

from rag.document_qa import (
    answer_document_query
)

from evaluation.evaluator import (
    run_evaluation
)

SESSION_ID = str(uuid.uuid4())


def get_response(user_input: str):

    try:

        # =========================
        # RUN GUARDRAILS
        # =========================

        guardrail_result = run_guardrails(
            user_input
        )

        if guardrail_result["blocked"]:

            return default_response(

                summary=guardrail_result["response"],

                response_type="guardrail"
            )

        # =========================
        # BUILD RAG CONTEXT
        # =========================

        rag_context = build_rag_context(
            user_input
        )

        enhanced_input = f"""

        User Query:
        {user_input}

        {rag_context}

        """
        # =========================
        # DOCUMENT QA ROUTING
        # =========================

        if is_document_query(user_input):

            doc_response = answer_document_query(
                user_input
            )

            return default_response(

                summary=doc_response,

                response_type="document_qa"
            )
        # =========================
        # AGENT INVOCATION
        # =========================

        result = insurance_agent.invoke(

            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            },

            config={
                "configurable": {
                    "thread_id": SESSION_ID
                }
            }
        )

        # =========================
        # EXTRACT RESPONSE
        # =========================

        raw_response = result[
            "messages"
        ][-1].content

        # =========================
        # SAFE JSON PARSING
        # =========================

        # =========================
        # SAFE JSON EXTRACTION
        # =========================

        parsed_json = extract_json(
            raw_response
        )

        if not parsed_json:

            parsed_response = default_response(

                summary=(
                    "Unable to process the response correctly."
                ),

                response_type="error"
            )

        else:

            validated_response = validate_response(
                parsed_json
            )

            if validated_response:

                parsed_response = validated_response

            else:

                parsed_response = default_response(

                    summary=(
                        "The response format was invalid."
                    ),

                    response_type="error"
                )

        # =========================
        # LOGGING
        # =========================

        log_interaction(

            session_id=SESSION_ID,

            user_query=user_input,

            response=str(parsed_response)
        )

        # =====================================
        # RUN LLM EVALUATION
        # =====================================

        evaluation_result = run_evaluation(

            query=user_input,

            response=parsed_response.get(
                "summary",
                ""
            )
        )

        parsed_response[
            "evaluation"
        ] = evaluation_result
        
        return parsed_response

    except Exception as e:

        print(f"Agent error: {e}")

        fallback_message = handle_llm_error(e)

        return default_response(

            summary=fallback_message,

            response_type="error"
        )