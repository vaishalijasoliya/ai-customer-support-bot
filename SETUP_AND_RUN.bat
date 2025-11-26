@echo off
echo ========================================
echo Complete Setup and Run
echo ========================================
echo.

REM Create .env file
echo Creating .env file...
(
echo OPENAI_API_KEY=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
echo CHATBOT_NAME=SupportBot
echo COMPANY_NAME=Your Company
echo TEMPERATURE=0.7
echo MAX_TOKENS=500
) > .env
echo .env file created!

echo.
echo Installing dependencies (this may take a few minutes)...
pip install -r requirements.txt

echo.
echo Setting up knowledge base...
python setup_knowledge_base.py

echo.
echo ========================================
echo Starting the bot...
echo ========================================
echo.
streamlit run app.py

