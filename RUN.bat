@echo off
echo ========================================
echo AI Customer Support Bot - Quick Setup
echo ========================================
echo.

echo Step 1: Creating .env file...
(
echo OPENAI_API_KEY=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
echo CHATBOT_NAME=SupportBot
echo COMPANY_NAME=Your Company
echo TEMPERATURE=0.7
echo MAX_TOKENS=500
) > .env
echo .env file created!

echo.
echo Step 2: Installing dependencies...
pip install -r requirements.txt

echo.
echo Step 3: Setting up knowledge base...
python setup_knowledge_base.py

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Now run: streamlit run app.py
echo.
pause

