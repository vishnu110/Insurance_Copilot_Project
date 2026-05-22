from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from tools.policy_ranking import policy_ranking_tool
from tools.needs_assessment import needs_assessment_tool
from tools.policy_comparison import policy_comparison_tool
from tools.premium_estimator import premium_estimator_tool
from langchain_core.output_parsers import JsonOutputParser

from schemas.models import InsuranceResponse
from memory.memory_manager import checkpointer

from dotenv import load_dotenv
load_dotenv()

# LLM
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.3
)

parser = JsonOutputParser(
    pydantic_object=InsuranceResponse
)

# Tools
tools = [
    needs_assessment_tool,
    policy_comparison_tool,
    premium_estimator_tool,
    policy_ranking_tool
]


# System Prompt
system_prompt = f"""
You are an advanced Insurance AI Copilot.

You help users:
- choose insurance
- compare policies
- estimate premiums
- identify coverage gaps

Guidelines:
- Be conversational and natural
- Ask follow-up questions only when necessary
- Use tools intelligently
- Avoid robotic responses
- For greetings, reply naturally
- For insurance queries, provide structured responses
- If insufficient or unrealistic information is provided, ask clarifying questions instead of inventing assumptions.
    If a tool returns a validation error,
    politely ask the user for corrected information.
    Do not invent values.
IMPORTANT:
Always respond ONLY in valid JSON.

Use this format exactly:

{parser.get_format_instructions()}
"""

# Agent
insurance_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt,
    checkpointer=checkpointer
)