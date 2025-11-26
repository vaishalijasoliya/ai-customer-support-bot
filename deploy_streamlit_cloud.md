# 🚀 Quick Deploy to Streamlit Cloud (5 Minutes!)

## Step 1: Push to GitHub

### If you don't have GitHub repo yet:

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "AI Customer Support Bot - Ready for deployment"

# Create repo on GitHub.com, then:
git remote add origin https://github.com/YOUR_USERNAME/ai-customer-support-bot.git
git branch -M main
git push -u origin main
```

### If you already have GitHub repo:

```bash
git add .
git commit -m "Update for deployment"
git push
```

## Step 2: Deploy to Streamlit Cloud

1. **Go to:** https://share.streamlit.io
2. **Sign in** with GitHub
3. **Click "New app"**
4. **Select:**
   - Repository: `your-username/ai-customer-support-bot`
   - Branch: `main`
   - Main file: `app_customer.py`
5. **Click "Deploy"**
6. **Wait 2 minutes** - Done! ✅

## Step 3: Configure Secrets

1. **In Streamlit Cloud**, go to your app
2. **Click "Settings"** (⚙️ icon)
3. **Click "Secrets"**
4. **Add these:**

```toml
OPENAI_API_KEY = "sk-your-api-key-here"
COMPANY_NAME = "Your Company Name"
CHATBOT_NAME = "SupportBot"
TEST_MODE = "false"
TEMPERATURE = "0.7"
MAX_TOKENS = "500"
ADMIN_PASSWORD = "your-secure-password"
```

5. **Save** - App will restart automatically

## Step 4: Get Your URL

Your app is now live at:
```
https://your-app-name.streamlit.app
```

**Share this URL with customers!** 🎉

## 🎯 For Admin Panel

Deploy separately:
1. Create another app in Streamlit Cloud
2. Use `app_admin.py` as main file
3. Same secrets
4. Different URL (private)

## ✅ Done!

Your chatbot is now:
- ✅ Live and accessible
- ✅ Public customer interface
- ✅ Ready for customers
- ✅ Free hosting!

**That's it!** 🚀

