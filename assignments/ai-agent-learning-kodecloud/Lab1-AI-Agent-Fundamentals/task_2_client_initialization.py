#!/usr/bin/env python3
"""
Task 2: Initialize the OpenAI Client
Learn how to connect to OpenAI's servers.
"""

import openai
import os

# The OpenAI client needs two things:
# 1. API Key - Your authentication (like a password)
# 2. Base URL - Where to send requests (like an address)

# TODO: Initialize the OpenAI client
# client = openai.OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY"),  
#     base_url=os.getenv("OPENAI_API_BASE")  
# )

# print("✅ Step 2 Complete: Connected to Ollama!")
# print(f"- API Key: {os.getenv('OPENAI_API_KEY')}...")
# print(f"- Base URL: {os.getenv('OPENAI_API_BASE')}")

client = openai.OpenAI (
    # api_key="ollama",  
    # base_url="http://localhost:11434/v1"
    api_key=os.getenv("OPENAI_API_KEY"),   
    base_url=os.getenv("OPENAI_API_BASE") 
)

print("✅ Step 2 Complete: Connected!")
print(f"- API Key: {client.api_key}...")
print(f"- Base URL: {client.base_url}")


# Create marker
os.makedirs("/root/markers", exist_ok=True)
with open("/root/markers/task2_client_complete.txt", "w") as f:
    f.write("SUCCESS")
