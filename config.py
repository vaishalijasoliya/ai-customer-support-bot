"""
Configuration file for AI Customer Support Bot
"""
import os
from dotenv import load_dotenv

# Try to import streamlit for cloud deployment
try:
    import streamlit as st
    USE_STREAMLIT_SECRETS = True
except:
    USE_STREAMLIT_SECRETS = False

load_dotenv()

# API Configuration - Check Streamlit secrets first (for cloud), then .env
if USE_STREAMLIT_SECRETS:
    try:
        OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY", ""))
        OPENAI_MODEL = st.secrets.get("OPENAI_MODEL", os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"))
        TEST_MODE = str(st.secrets.get("TEST_MODE", os.getenv("TEST_MODE", "False"))).lower() == "true"
        CHATBOT_NAME = st.secrets.get("CHATBOT_NAME", os.getenv("CHATBOT_NAME", "SupportBot"))
        COMPANY_NAME = st.secrets.get("COMPANY_NAME", os.getenv("COMPANY_NAME", "Your Company"))
        TEMPERATURE = float(st.secrets.get("TEMPERATURE", os.getenv("TEMPERATURE", "0.7")))
        MAX_TOKENS = int(st.secrets.get("MAX_TOKENS", os.getenv("MAX_TOKENS", "500")))
    except:
        # Fallback to environment variables if secrets not available
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
        OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        TEST_MODE = os.getenv("TEST_MODE", "False").lower() == "true"
        CHATBOT_NAME = os.getenv("CHATBOT_NAME", "SupportBot")
        COMPANY_NAME = os.getenv("COMPANY_NAME", "Your Company")
        TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
        MAX_TOKENS = int(os.getenv("MAX_TOKENS", "500"))
else:
    # Local development - use .env file
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    TEST_MODE = os.getenv("TEST_MODE", "False").lower() == "true"
    CHATBOT_NAME = os.getenv("CHATBOT_NAME", "SupportBot")
    COMPANY_NAME = os.getenv("COMPANY_NAME", "Your Company")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "500"))

# Knowledge Base Settings
KNOWLEDGE_BASE_DIR = "knowledge_base"
VECTOR_STORE_DIR = "vector_store"

# System Prompt Template
SYSTEM_PROMPT = f"""You are {CHATBOT_NAME}, a helpful and professional AI customer support assistant for {COMPANY_NAME}.

Your role is to:
- Provide accurate, friendly, and helpful responses to customer inquiries
- Answer questions based on the provided knowledge base
- Escalate complex issues to human support when necessary
- Maintain a professional and empathetic tone
- If you don't know something, admit it and offer to connect them with human support

Guidelines:
- Be concise but thorough
- Use clear, simple language
- Show empathy for customer concerns
- Always offer next steps or solutions
- End responses with a helpful question or suggestion

Remember: You represent {COMPANY_NAME}, so be professional and helpful at all times."""


