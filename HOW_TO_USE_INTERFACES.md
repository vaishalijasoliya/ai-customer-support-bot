# 📱 How to Use Customer & Admin Interfaces

## 🎯 Two Separate Interfaces

You now have **TWO separate apps**:

### 1. Customer Interface (`app_customer.py`)
**For:** End users, customers, website visitors
**Features:**
- ✅ Clean chat interface
- ✅ NO admin features visible
- ✅ Professional appearance
- ✅ Just chat - that's it!

### 2. Admin Interface (`app_admin.py`)
**For:** Business owners, admins, you
**Features:**
- ✅ Manage FAQs
- ✅ Add documents
- ✅ Test chat
- ✅ View analytics
- ✅ Configure settings
- ✅ Password protected

## 🚀 How to Run

### Option 1: Run Both Separately (Recommended)

**Terminal 1 - Customer Interface:**
```bash
streamlit run app_customer.py --server.port 8501
```
Access at: http://localhost:8501

**Terminal 2 - Admin Interface:**
```bash
streamlit run app_admin.py --server.port 8502
```
Access at: http://localhost:8502

### Option 2: Use the Old Combined Interface

If you want the old combined interface (for testing):
```bash
streamlit run app.py
```

## 🔐 Admin Password

**Default password:** `admin123`

**To change it:**
1. Add to your `.env` file:
   ```
   ADMIN_PASSWORD=your_secure_password_here
   ```
2. Restart the admin app

## 📋 Usage Workflow

### For Admins:
1. **Start admin panel:**
   ```bash
   streamlit run app_admin.py
   ```

2. **Login** with password

3. **Add FAQs/Documents** in the Knowledge Base tab

4. **Test** in the Test Chat tab

5. **Deploy customer interface** separately

### For Customers:
1. **Access customer interface:**
   ```bash
   streamlit run app_customer.py
   ```

2. **Just chat** - clean interface, no admin features

## 🎨 Interface Comparison

| Feature | Customer Interface | Admin Interface |
|---------|-------------------|-----------------|
| Chat | ✅ Yes | ✅ Yes (for testing) |
| Add FAQ | ❌ No | ✅ Yes |
| Add Document | ❌ No | ✅ Yes |
| Settings | ❌ No | ✅ Yes |
| Analytics | ❌ No | ✅ Yes |
| Password | ❌ No | ✅ Yes |

## 💡 Production Deployment

### For Production:

1. **Customer Interface:**
   - Deploy to public URL
   - Embed in website
   - No password needed

2. **Admin Interface:**
   - Deploy to private URL
   - Password protected
   - Only admins access

### Example URLs:
- Customer: `https://yourcompany.com/chat`
- Admin: `https://admin.yourcompany.com` (private)

## 🔧 Customization

### Customer Interface:
- Edit `app_customer.py`
- Change colors, layout, branding
- Add company logo
- Customize welcome message

### Admin Interface:
- Edit `app_admin.py`
- Add more admin features
- Customize tabs
- Add more analytics

## ✅ Benefits

1. **Professional:** Customers don't see admin features
2. **Secure:** Admin panel is password protected
3. **Clean:** Each interface has its purpose
4. **Scalable:** Easy to deploy separately
5. **Better UX:** Right features for right users

## 🚀 Quick Start

1. **Test customer interface:**
   ```bash
   streamlit run app_customer.py
   ```

2. **Test admin interface:**
   ```bash
   streamlit run app_admin.py
   ```
   Password: `admin123`

3. **Add some FAQs** in admin panel

4. **Test chat** in customer interface

That's it! 🎉

