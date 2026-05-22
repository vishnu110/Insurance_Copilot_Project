import json
from datetime import datetime


LOG_FILE = "logs/chatbot_logs.jsonl"


def log_interaction(session_id, user_query, response):
    log_data = {
        "timestamp": str(datetime.now()),
        "session_id": session_id,
        "user_query": user_query,
        "response": response
    }

    with open(LOG_FILE, "a") as file:
        file.write(json.dumps(log_data) + "\n")