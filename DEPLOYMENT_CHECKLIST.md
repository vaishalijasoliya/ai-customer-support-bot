# ✅ Deployment Checklist

## Before Deploying

### Code Preparation
- [ ] Test locally - Everything works
- [ ] Remove test data
- [ ] Clean up code
- [ ] Update README
- [ ] Add .gitignore

### Configuration
- [ ] Set TEST_MODE=false (for production)
- [ ] Update COMPANY_NAME
- [ ] Set CHATBOT_NAME
- [ ] Configure ADMIN_PASSWORD
- [ ] Add real API key (client's key)

### Knowledge Base
- [ ] Add client's FAQs
- [ ] Add company documents
- [ ] Test knowledge base
- [ ] Verify responses

### Security
- [ ] Never commit .env file
- [ ] Use environment variables
- [ ] Set strong admin password
- [ ] Remove test API keys

## Deployment Steps

### GitHub Setup
- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Verify all files uploaded
- [ ] Check .gitignore working

### Streamlit Cloud
- [ ] Sign in to Streamlit Cloud
- [ ] Connect GitHub account
- [ ] Create new app
- [ ] Select app_customer.py
- [ ] Configure secrets/environment variables
- [ ] Deploy and test

### Admin Panel (Separate)
- [ ] Deploy app_admin.py separately
- [ ] Set admin password
- [ ] Test login
- [ ] Verify admin features work

## After Deployment

### Testing
- [ ] Test customer interface
- [ ] Test chat functionality
- [ ] Test knowledge base
- [ ] Test admin panel
- [ ] Verify API working

### Client Handover
- [ ] Provide customer URL
- [ ] Provide admin URL and password
- [ ] Show how to add FAQs
- [ ] Document everything
- [ ] Provide support contact

### Monitoring
- [ ] Set up API usage alerts
- [ ] Monitor errors
- [ ] Check logs regularly
- [ ] Track costs

## Quick Reference

### Customer URL
```
https://your-app-name.streamlit.app
```

### Admin URL
```
https://your-admin-app.streamlit.app
```

### Environment Variables Needed
```
OPENAI_API_KEY
COMPANY_NAME
CHATBOT_NAME
TEST_MODE
ADMIN_PASSWORD
```

## ✅ Ready to Deploy!

Follow the checklist and you're good to go! 🚀

