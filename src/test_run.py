import os
from chat_session import ChatSession
from log_analyzer import analyze_log
from retriever import LogRetriever

# Load log
log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "sample.log")

with open(log_path) as f:
    log_data = f.read()

# Build retriever
retriever = LogRetriever(log_data)

# Chat session
chat = ChatSession()

print("\n=== Log Debug AI V3 (Type 'exit' to quit) ===\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    relevant_chunks = retriever.get_relevant_chunks(user_input)

    context = "\n\n".join(relevant_chunks)

    messages = [
        {
            "role": "system",
            "content": f"""
You are a network log debugging expert.

Relevant log data:
{context}
"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    response = analyze_log(messages)

    print("\nAI:", response, "\n")
