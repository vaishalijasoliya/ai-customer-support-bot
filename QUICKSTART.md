# 🚀 Quick Start Guide

Get your AI Customer Support Bot running in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Get OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Create a new API key
4. Copy the key

## Step 3: Configure

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` and add your API key:
   ```
   OPENAI_API_KEY=sk-your-key-here
   CHATBOT_NAME=SupportBot
   COMPANY_NAME=Your Company
   ```

## Step 4: Set Up Knowledge Base (Optional)

```bash
python setup_knowledge_base.py
```

This adds sample FAQs. You can customize them later.

## Step 5: Run the Bot!

```bash
streamlit run app.py
```

Your browser will open automatically to `http://localhost:8501`

## 🎉 You're Done!

Start chatting with your bot. You can:
- Add FAQs via the sidebar
- Add documents via the sidebar
- Customize the bot name and company in `.env`

## 💡 Tips

- **Free Tier**: OpenAI offers free credits when you sign up
- **Cost Control**: Use `gpt-3.5-turbo` instead of `gpt-4` for lower costs (edit `config.py`)
- **Testing**: Start with the free tier, then scale up

## 🐛 Troubleshooting

**"No module named 'openai'"**
→ Run: `pip install -r requirements.txt`

**"OpenAI API key not found"**
→ Make sure `.env` file exists and has your API key

**"Streamlit not found"**
→ Run: `pip install streamlit`

---

**Ready to sell on Upwork?** Check the README.md for deployment and customization tips!


