# 🏢 How to Change Company Name

## Quick Method (Easiest)

### Option 1: Edit .env File Directly

1. **Open `.env` file** in your project folder
2. **Find this line:**
   ```
   COMPANY_NAME=Your Company
   ```
3. **Change it to your company name:**
   ```
   COMPANY_NAME=Acme Corporation
   ```
4. **Save the file**
5. **Restart your Streamlit app**

### Option 2: Use Python Script

Run this command:
```bash
python change_company.py "Your New Company Name"
```

## 📝 What Gets Changed

When you change the company name, it updates:
- ✅ Chatbot header/title
- ✅ System prompt (how bot introduces itself)
- ✅ Footer text
- ✅ Admin panel display
- ✅ All references throughout the app

## 🎯 Example

**Before:**
```
COMPANY_NAME=Your Company
```

**After:**
```
COMPANY_NAME=Tech Solutions Inc
```

## 🔄 After Changing

1. **Restart Streamlit:**
   - Stop the current app (Ctrl+C)
   - Run: `streamlit run app_customer.py`
   - Or: `streamlit run app_admin.py`

2. **The new name will appear:**
   - In the header
   - In chat responses
   - In admin panel

## 💡 Pro Tip

You can also change:
- `CHATBOT_NAME` - Name of the bot itself
- Both together for complete branding

Example:
```
CHATBOT_NAME=Alex
COMPANY_NAME=Tech Solutions Inc
```

Result: "Alex - Tech Solutions Inc Customer Support"

