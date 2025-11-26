# AI Customer Support Bot 🤖

A professional AI-powered customer support chatbot that can be customized for any business. Built with OpenAI GPT, Streamlit, and LangChain.

## ✨ Features

- **24/7 AI Customer Support**: Automated responses using GPT-3.5/GPT-4
- **Knowledge Base Integration**: Train the bot with custom FAQs and documents
- **Web Interface**: Beautiful Streamlit-based chat interface
- **Multi-turn Conversations**: Maintains context throughout the conversation
- **Easy Customization**: Simple configuration for different businesses
- **Vector Search**: Semantic search through knowledge base using embeddings

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone or download this project**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   # Copy the example env file
   cp .env.example .env
   
   # Edit .env and add your OpenAI API key
   OPENAI_API_KEY=your_api_key_here
   CHATBOT_NAME=SupportBot
   COMPANY_NAME=Your Company Name
   ```

4. **Set up initial knowledge base** (optional):
   ```bash
   python setup_knowledge_base.py
   ```

5. **Run the chatbot**:
   ```bash
   streamlit run app.py
   ```

6. **Open your browser** to `http://localhost:8501`

## 📁 Project Structure

```
ai-customer-support-bot/
├── app.py                      # Streamlit web interface
├── chatbot.py                  # Main chatbot engine
├── knowledge_base_manager.py   # Knowledge base management
├── config.py                  # Configuration settings
├── setup_knowledge_base.py    # Initial knowledge base setup
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── knowledge_base/            # Knowledge base documents (auto-created)
└── vector_store/              # Vector embeddings (auto-created)
```

## 🎯 Usage

### Basic Usage

1. Start the app: `streamlit run app.py`
2. Type your question in the chat interface
3. The bot will respond using the knowledge base and AI

### Adding Knowledge

#### Via Web Interface:
- Use the sidebar to add FAQs or documents
- Click "Add FAQ" to add question-answer pairs
- Click "Add Document" to add longer content

#### Via Code:
```python
from chatbot import CustomerSupportBot

bot = CustomerSupportBot()

# Add a FAQ
bot.add_faq("What is your return policy?", "We offer 30-day returns...")

# Add a document
bot.add_knowledge("Your company information here...")
```

## ⚙️ Configuration

Edit `config.py` or `.env` file to customize:

- **CHATBOT_NAME**: Name of your chatbot
- **COMPANY_NAME**: Your company name
- **OPENAI_MODEL**: Choose `gpt-3.5-turbo` (cheaper) or `gpt-4` (better quality)
- **TEMPERATURE**: Controls randomness (0.0-1.0)
- **MAX_TOKENS**: Maximum response length

## 💰 Cost Considerations

### Free Tier Options:
- **OpenAI**: Free tier available (limited usage)
- **Hosting**: Railway.app, Render.com offer free tiers
- **Development**: All tools are free to use

### Production Costs:
- **OpenAI API**: ~$0.50-$2 per 1M tokens (GPT-3.5-turbo)
- **Hosting**: $5-$20/month for small-medium traffic
- **Total**: ~$50-$200/month for typical usage

**Recommendation**: Have clients pay for their own API usage directly.

## 🔧 Customization for Clients

### For Upwork Projects:

1. **Customize Branding**:
   - Update `CHATBOT_NAME` and `COMPANY_NAME` in `.env`
   - Modify system prompt in `config.py`

2. **Add Client's Knowledge Base**:
   - Import their FAQs
   - Add product/service documentation
   - Include company policies

3. **Deploy**:
   - Deploy to Railway.app, Render.com, or similar
   - Set up client's OpenAI API key
   - Provide access credentials

## 📦 Deployment Options

### Option 1: Railway.app (Recommended)
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

### Option 2: Render.com
- Connect your GitHub repo
- Set environment variables
- Deploy automatically

### Option 3: Streamlit Cloud
- Push to GitHub
- Connect to Streamlit Cloud
- Deploy for free

## 🎨 Customization Examples

### Change Chatbot Personality:
Edit `SYSTEM_PROMPT` in `config.py`:
```python
SYSTEM_PROMPT = """You are a friendly, casual support assistant..."""
```

### Add WhatsApp Integration:
Use Twilio API or WhatsApp Business API to extend functionality.

### Add CRM Integration:
Integrate with Salesforce, HubSpot, or Zendesk APIs.

## 📊 Pricing Strategy for Upwork

### Starter Package ($500-$1,500):
- Basic chatbot setup
- 20-50 FAQs
- Website integration
- 1 month support

### Professional Package ($2,000-$4,000):
- Custom AI training
- Multi-channel integration
- CRM integration
- Analytics dashboard
- 3 months support

### Enterprise Package ($5,000+):
- Full customization
- All integrations
- Advanced features
- Ongoing maintenance

## 🐛 Troubleshooting

### "OpenAI API key not found"
- Make sure `.env` file exists and contains `OPENAI_API_KEY`
- Check that the key is valid

### "No module named 'openai'"
- Run `pip install -r requirements.txt`

### Knowledge base not working
- Run `python setup_knowledge_base.py` to initialize
- Check that `vector_store/` directory exists

## 📝 License

This project is open source and available for commercial use.

## 🤝 Support

For questions or issues:
- Check the documentation
- Review the code comments
- Contact the developer

## 🚀 Next Steps

1. ✅ Set up your OpenAI API key
2. ✅ Customize for your first client
3. ✅ Build your portfolio
4. ✅ Start offering on Upwork!

---

**Built with ❤️ for Upwork freelancers**


