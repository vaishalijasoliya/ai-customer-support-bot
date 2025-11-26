"""Quick setup script to create .env file"""
import os

env_content = """OPENAI_API_KEY=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
CHATBOT_NAME=SupportBot
COMPANY_NAME=Your Company
TEMPERATURE=0.7
MAX_TOKENS=500
"""

with open('.env', 'w') as f:
    f.write(env_content)

print("✅ .env file created successfully!")




