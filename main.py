# app.py

from fastapi import FastAPI
from pydantic import BaseModel

from chatbot import get_response, SESSION_ID
from memory.memory_manager import clear_memory

app = FastAPI(title="Insurance Policy Co-Pilot")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Insurance Policy Co-Pilot Running"}

@app.post("/chat")
def chat(request: ChatRequest):
    response = get_response(request.message)
    return {"user_message": request.message, "assistant_response": response}

@app.post("/reset")
def reset_memory():
    clear_memory(SESSION_ID)
    return {"message": "Conversation memory cleared"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "model": "gpt-4o-mini"}