import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get GitHub token from .env
token = os.getenv("GITHUB_TOKEN")

# GitHub Models endpoint
endpoint = "https://models.github.ai/inference"

# Model name (GitHub hosted)
model = "openai/gpt-4.1-mini"

# Create client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def analyze_log(messages):

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content

