# memory/memory_manager.py

from langgraph.checkpoint.memory import MemorySaver

# In-memory checkpointer — persists conversation per thread_id
checkpointer = MemorySaver()

def clear_memory(session_id: str):
    # MemorySaver stores by thread_id; delete its entry
    if session_id in checkpointer.storage:
        del checkpointer.storage[session_id]