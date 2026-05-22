import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://localhost:8000"
# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Insurance AI Copilot",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.stApp { background-color: #0B0F19; color: white; }
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container { padding-top: 1.5rem; max-width: 1000px; }

.main-title { font-size: 1.7rem; font-weight: 700; color: white; margin-bottom: 0; }
.sub-title { color: #94A3B8; font-size: 0.88rem; margin-bottom: 1.5rem; }

.summary-box {
    background: #172554; padding: 12px 14px; font-size: 0.9rem;
    border-radius: 14px; margin-bottom: 12px; line-height: 1.5;
}
.recommend-box {
    background-color: #052E16; border: 1px solid #14532D;
    padding: 8px 12px; font-size: 0.88rem; border-radius: 12px;
    margin-bottom: 8px; line-height: 1.4;
}
.gap-box {
    background-color: #3F1D1D; border: 1px solid #7F1D1D;
    padding: 8px 12px; font-size: 0.88rem; border-radius: 12px;
    margin-bottom: 8px; line-height: 1.4;
}
[data-testid="metric-container"] {
    background: #111827; border: 1px solid #1F2937;
    padding: 10px; border-radius: 14px;
}
[data-testid="stDataFrame"] { border-radius: 14px; overflow: hidden; }
.stChatInputContainer {
    background-color: #0B0F19; border-top: 1px solid #1F2937; padding-top: 12px;
}
textarea {
    background-color: #1F2937 !important; color: white !important;
    border-radius: 14px !important; font-size: 0.92rem !important;
}
.stButton button {
    border-radius: 12px; background-color: #2563EB; color: white;
    border: none; padding: 8px 16px; font-weight: 600;
}
.element-container { margin-bottom: 0.5rem !important; }

/* Animated thinking dots */
@keyframes thinking-bounce {
    0%, 60%, 100% { transform: translateY(0);    opacity: 0.35; }
    30%            { transform: translateY(-7px); opacity: 1;    }
}
.thinking-dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: #60A5FA; display: inline-block;
    animation: thinking-bounce 1.2s infinite ease-in-out;
}
.thinking-dot:nth-child(1) { animation-delay: 0s;   }
.thinking-dot:nth-child(2) { animation-delay: 0.2s; }
.thinking-dot:nth-child(3) { animation-delay: 0.4s; }

</style>
""", unsafe_allow_html=True)


# =========================================
# HEADER
# =========================================

st.markdown("""
<div class="main-title">🛡️ Insurance AI Copilot</div>
<div class="sub-title">
    AI-powered insurance recommendations, premium estimation, and policy comparison platform.
</div>
""", unsafe_allow_html=True)


# =========================================
# TOP ACTIONS
# =========================================

_, top_col2 = st.columns([9, 1])

with top_col2:
    if st.button("↺"):
        try:
            requests.post(f"{API_BASE_URL}/reset")
        except requests.exceptions.ConnectionError:
            st.warning("Backend not reachable.")
        st.session_state.messages = []
        st.session_state.is_thinking = False
        st.session_state.pending_input = ""
        st.rerun()


# =========================================
# SESSION STATE
# =========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# is_thinking=True means user message stored, waiting for backend
if "is_thinking" not in st.session_state:
    st.session_state.is_thinking = False

if "pending_input" not in st.session_state:
    st.session_state.pending_input = ""


# =========================================
# HELPER: render one message bubble
# =========================================

def render_message(message: dict):
    role = message["role"]

    if role == "user":
        st.markdown(
            f"""
            <div style="display:flex;justify-content:flex-end;
                        margin-top:12px;margin-bottom:12px;">
                <div style="background:#1E293B;border:1px solid #334155;
                            border-radius:16px;padding:12px 16px;
                            font-size:0.92rem;line-height:1.5;
                            max-width:70%;color:white;">
                    {message["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="display:flex;align-items:flex-start;gap:10px;
                        margin-top:12px;margin-bottom:12px;">
                <div style="width:32px;height:32px;border-radius:50%;
                            background:#1E3A8A;display:flex;
                            align-items:center;justify-content:center;
                            font-size:0.9rem;flex-shrink:0;">🤖</div>
                <div style="background:#111827;border:1px solid #1F2937;
                            border-radius:16px;padding:12px 16px;
                            font-size:0.92rem;line-height:1.5;
                            max-width:70%;color:white;">
                    {message["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # PREMIUM DETAILS
        premium = message.get("premium_details", {})
        if premium and any(
            isinstance(v, (int, float)) and v != 0 for v in premium.values()
        ):
            st.markdown("#### 💰 Premium Details")
            cols = st.columns(len(premium))
            for i, (key, value) in enumerate(premium.items()):
                with cols[i]:
                    st.metric(key.replace("_", " ").title(), value)

        # POLICY COMPARISON
        comparisons = message.get("policy_comparisons", [])
        if comparisons:
            st.markdown("#### 📊 Policy Comparison")
            st.dataframe(pd.DataFrame(comparisons), use_container_width=True)


# =========================================
# RENDER CHAT HISTORY
# =========================================

for message in st.session_state.messages:
    render_message(message)


# =========================================
# THINKING INDICATOR (rendered below history)
# Visible while is_thinking=True
# =========================================

thinking_slot = st.empty()

if st.session_state.is_thinking:
    thinking_slot.markdown(
        """
        <div style="display:flex;align-items:flex-start;gap:10px;
                    margin-top:12px;margin-bottom:12px;">
            <div style="width:32px;height:32px;border-radius:50%;
                        background:#1E3A8A;display:flex;
                        align-items:center;justify-content:center;
                        font-size:0.9rem;flex-shrink:0;">🤖</div>
            <div style="background:#111827;border:1px solid #1F2937;
                        border-radius:16px;padding:14px 20px;
                        display:flex;align-items:center;gap:12px;
                        color:#94A3B8;font-size:0.88rem;">
                <span>Thinking</span>
                <span style="display:inline-flex;gap:6px;align-items:center;">
                    <span class="thinking-dot"></span>
                    <span class="thinking-dot"></span>
                    <span class="thinking-dot"></span>
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================
# CHAT INPUT
# =========================================

user_input = st.chat_input("Ask anything about insurance...")


# =========================================
# STEP 1 — User hits send
#   • Append user bubble to history immediately
#   • Set is_thinking = True
#   • Rerun → user sees their message + thinking dots right away
# =========================================

if user_input and not st.session_state.is_thinking:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    st.session_state.is_thinking = True
    st.session_state.pending_input = user_input
    st.rerun()


# =========================================
# STEP 2 — On rerun while is_thinking=True
#   • Thinking dots are already visible on screen
#   • Call backend (blocking)
#   • Append assistant response
#   • Clear thinking flag → rerun cleanly
# =========================================

if st.session_state.is_thinking:
    pending = st.session_state.pending_input

    try:
        api_response = requests.post(
            f"{API_BASE_URL}/chat",
            json={"message": pending},
            timeout=60
        )
        api_response.raise_for_status()
        result = api_response.json()
        assistant_response = result["assistant_response"]

    except requests.exceptions.ConnectionError:
        assistant_response = {
            "summary": "❌ Backend not reachable. Please start the FastAPI server.",
            "recommendations": [], "coverage_gaps": [],
            "premium_details": {}, "policy_comparisons": []
        }

    except requests.exceptions.HTTPError as e:
        assistant_response = {
            "summary": f"❌ API error: {e}",
            "recommendations": [], "coverage_gaps": [],
            "premium_details": {}, "policy_comparisons": []
        }

    # Parse response fields
    summary            = assistant_response.get("summary", "")
    recommendations    = assistant_response.get("recommendations", [])
    coverage_gaps      = assistant_response.get("coverage_gaps", [])
    premium_details    = assistant_response.get("premium_details", {})
    policy_comparisons = assistant_response.get("policy_comparisons", [])

    # Build formatted HTML content
    formatted_response = ""

    if summary:
        formatted_response += f'<div class="summary-box">{summary}</div>'

    if recommendations:
        formatted_response += "Recommendations\n"
        for rec in recommendations:
            formatted_response += f'<div class="recommend-box">{rec}</div>'

    if coverage_gaps:
        formatted_response += "Coverage Gaps\n"
        for gap in coverage_gaps:
            formatted_response += f'<div class="gap-box">{gap}</div>'

    # Store assistant message and clear thinking state
    st.session_state.messages.append({
        "role": "assistant",
        "content": formatted_response,
        "premium_details": premium_details,
        "policy_comparisons": policy_comparisons
    })

    st.session_state.is_thinking = False
    st.session_state.pending_input = ""
    thinking_slot.empty()
    st.rerun()