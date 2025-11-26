# 🧪 Test Mode / Sandbox Mode Guide

## What is Test Mode?

Test Mode allows you to **test your chatbot code completely FREE** without making any API calls to OpenAI. Perfect for:
- Testing the UI and functionality
- Developing and debugging
- Showing clients the interface
- Learning how the bot works
- No API costs at all!

## 🚀 How to Enable Test Mode

### Option 1: Edit .env file (Recommended)

1. Open your `.env` file
2. Add or change this line:
   ```
   TEST_MODE=true
   ```
3. Save the file
4. Restart your Streamlit app

### Option 2: Set Environment Variable

**Windows (PowerShell):**
```powershell
$env:TEST_MODE="true"
streamlit run app.py
```

**Windows (CMD):**
```cmd
set TEST_MODE=true
streamlit run app.py
```

**Linux/Mac:**
```bash
export TEST_MODE=true
streamlit run app.py
```

## ✅ What Test Mode Does

- ✅ **Simulates AI responses** based on keywords and knowledge base
- ✅ **No API calls** - completely free!
- ✅ **Full functionality** - UI, knowledge base, conversation history all work
- ✅ **Realistic responses** - mimics how the bot would respond
- ✅ **Knowledge base integration** - uses your FAQs and documents

## 🎯 Test Mode Features

### 1. Keyword-Based Responses
Test mode recognizes common questions:
- "hello", "hi" → Greeting response
- "hours" → Business hours info
- "order" → Order tracking info
- "return" → Return policy
- "contact" → Contact information
- "shipping" → Shipping information
- And more!

### 2. Knowledge Base Integration
- If you've added FAQs, test mode will use them
- Documents in knowledge base are referenced
- Context-aware responses (simulated)

### 3. Default Responses
- For questions not matching keywords, provides helpful default response
- Explains that it's in test mode
- Suggests common topics

## 📝 Example Usage

### Enable Test Mode:
```bash
# Edit .env file
TEST_MODE=true

# Run the app
streamlit run app.py
```

### Test the Bot:
1. Ask: "What are your business hours?"
   - Response: Business hours information

2. Ask: "How can I track my order?"
   - Response: Order tracking instructions

3. Ask: "Hello"
   - Response: Friendly greeting

4. Ask: "Tell me about your return policy"
   - Response: Return policy details

## 🔄 Switching Between Modes

### Test Mode (Free):
```
TEST_MODE=true
```

### Production Mode (Uses API):
```
TEST_MODE=false
# or remove the line entirely
```

## 💡 When to Use Test Mode

✅ **Use Test Mode When:**
- You don't have API credits
- You want to test the UI
- You're developing/debugging
- You want to show clients the interface
- You're learning how the bot works

❌ **Don't Use Test Mode When:**
- You need real AI responses
- You're doing final testing
- You're deploying to production
- You need advanced AI capabilities

## 🎨 Customizing Test Mode Responses

You can customize test mode responses by editing the `_generate_mock_response()` method in `chatbot.py`.

## 🔍 Testing Checklist

With Test Mode enabled, you can test:
- [x] Chat interface works
- [x] Knowledge base (add FAQs)
- [x] Document management
- [x] Conversation history
- [x] Reset conversation
- [x] UI responsiveness
- [x] Error handling
- [x] All features except real AI

## 🚀 Quick Start

1. **Enable test mode:**
   ```bash
   # Edit .env
   TEST_MODE=true
   ```

2. **Run the app:**
   ```bash
   streamlit run app.py
   ```

3. **Start testing!**
   - No API key needed
   - No costs
   - Full functionality

## 📊 Test Mode vs Production Mode

| Feature | Test Mode | Production Mode |
|---------|-----------|-----------------|
| API Calls | ❌ None | ✅ Real API |
| Cost | 💰 FREE | 💰 Pay per use |
| Responses | 🎭 Simulated | 🤖 Real AI |
| Knowledge Base | ✅ Works | ✅ Works |
| UI | ✅ Full | ✅ Full |
| Real AI | ❌ No | ✅ Yes |

## 🎉 Benefits

- **100% Free** - No API costs
- **Full Testing** - Test all features
- **No Setup** - Just change one setting
- **Safe** - No risk of API charges
- **Fast** - Instant responses
- **Perfect for Development** - Test before going live

---

**Enjoy free testing! 🎉**

When you're ready for production, just set `TEST_MODE=false` and add your API key!

