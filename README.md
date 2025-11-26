# 🤖 AI Customer Support Bot

A professional AI-powered customer support chatbot built with OpenAI GPT, Streamlit, and LangChain. Perfect for businesses looking to automate customer support and reduce costs.

## ✨ Features

- **24/7 AI Customer Support** - Automated responses using GPT-3.5/GPT-4
- **Knowledge Base Integration** - Train the bot with custom FAQs and documents
- **Web Interface** - Beautiful Streamlit-based chat interface
- **Multi-turn Conversations** - Maintains context throughout conversations
- **Test Mode** - Test without API costs (FREE!)
- **Admin Panel** - Easy management of FAQs and documents
- **Separate Interfaces** - Clean customer interface + admin panel
- **Easy Deployment** - Deploy to Streamlit Cloud in minutes

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your OpenAI API key

# Run the app
streamlit run app_customer.py
```

### Test Mode (FREE!)

Enable test mode to test without API costs:

```bash
# In .env file
TEST_MODE=true
```

## 📁 Project Structure

```
ai-customer-support-bot/
├── app_customer.py          # Customer-facing chat interface
├── app_admin.py            # Admin panel for management
├── chatbot.py              # Main chatbot engine
├── knowledge_base_manager.py # Knowledge base system
├── config.py               # Configuration
└── requirements.txt        # Dependencies
```

## 🎯 Usage

### Customer Interface
```bash
streamlit run app_customer.py
```
Clean chat interface for end users.

### Admin Panel
```bash
streamlit run app_admin.py
```
Manage FAQs, documents, and settings.

## 🚀 Deployment

### Streamlit Cloud (Recommended - FREE!)

1. Push to GitHub
2. Go to: https://share.streamlit.io
3. Connect GitHub and deploy
4. Configure environment variables
5. Done!

See `DEPLOYMENT_GUIDE.md` for detailed instructions.

## ⚙️ Configuration

Edit `.env` file:
```
OPENAI_API_KEY=your_key_here
COMPANY_NAME=Your Company
CHATBOT_NAME=SupportBot
TEST_MODE=false
```

## 💰 Pricing

- **Hosting:** FREE on Streamlit Cloud
- **API Costs:** ~$50-200/month (client pays)
- **Setup:** Custom pricing per client

## 📚 Documentation

- `DEPLOYMENT_GUIDE.md` - Complete deployment guide
- `TEST_MODE_GUIDE.md` - How to use test mode
- `UPWORK_SALES_GUIDE.md` - Selling on Upwork
- `GITHUB_SETUP.md` - GitHub setup instructions

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** - Web interface
- **OpenAI GPT** - AI responses
- **LangChain** - AI framework
- **ChromaDB** - Vector storage

## 📝 License

Open source - Free for commercial use.

## 🤝 Support

For questions or issues, check the documentation files or create an issue.

---

**Built for Upwork freelancers and businesses** 🚀

