# 🔍 Troubleshooting: "Insufficient Quota" with $5 Credit

## The Problem
You have $5 credit but still getting "insufficient_quota" error.

## Common Causes & Solutions

### 1. ✅ Credits are for ChatGPT Plus, NOT API
**Issue:** The $5 might be for ChatGPT Plus (the chat interface), not for API usage.

**Check:**
- Go to: https://platform.openai.com/account/billing
- Look for "API Credits" vs "ChatGPT Plus Credits"
- They are **separate**!

**Fix:**
- You need to add credits specifically for **API usage**
- Minimum: $5 for API
- Add payment method and add API credits

### 2. ✅ API Key from Different Account
**Issue:** Your API key might be from Account A, but credits are on Account B.

**Check:**
1. Go to: https://platform.openai.com/api-keys
2. Check which account you're logged into
3. Go to: https://platform.openai.com/account/billing
4. Check if it's the same account

**Fix:**
- Make sure API key and credits are on the **same account**
- Or create API key on the account with credits

### 3. ✅ Account Needs Verification
**Issue:** Account might need phone/email verification.

**Check:**
- Go to: https://platform.openai.com/account
- Look for verification warnings

**Fix:**
- Complete account verification
- Add phone number if required

### 4. ✅ Spending Limit Set to $0
**Issue:** You have credits but spending limit is $0.

**Check:**
1. Go to: https://platform.openai.com/account/billing
2. Click "Limits" or "Usage limits"
3. Check "Hard limit" or "Soft limit"

**Fix:**
- Set spending limit to at least $5 (or higher)
- Or remove the limit entirely

### 5. ✅ Credits Not Activated
**Issue:** Credits might be pending or not activated.

**Check:**
- Go to: https://platform.openai.com/account/billing
- Check transaction history
- See if credits are "Pending" or "Active"

**Fix:**
- Wait for credits to activate (can take a few minutes)
- Contact OpenAI support if stuck

## 🔧 Step-by-Step Fix

### Step 1: Verify Account Status
```
1. Go to: https://platform.openai.com/account/billing
2. Check:
   - Current balance (should show $5+)
   - Account status (should be "Active")
   - Payment method (should be added)
```

### Step 2: Check API Usage Limits
```
1. Go to: https://platform.openai.com/account/billing/limits
2. Check:
   - Hard limit (should be $5+ or unlimited)
   - Soft limit (should be $5+ or unlimited)
3. If $0, increase it!
```

### Step 3: Verify API Key
```
1. Go to: https://platform.openai.com/api-keys
2. Check:
   - Key is from the same account
   - Key is not expired
   - Key has API access (not just ChatGPT Plus)
```

### Step 4: Test API Directly
Run our test script:
```bash
python test_api.py
```

### Step 5: Check Usage Dashboard
```
1. Go to: https://platform.openai.com/usage
2. Check:
   - API usage (should show your test calls)
   - Remaining credits
   - Any error messages
```

## 💡 Quick Fixes to Try

### Fix 1: Add Payment Method (Even with Credits)
Sometimes you need a payment method even if you have credits:
1. Go to: https://platform.openai.com/account/billing
2. Add credit card
3. Set spending limit to $10
4. Try again

### Fix 2: Create New API Key
Sometimes keys get corrupted:
1. Go to: https://platform.openai.com/api-keys
2. Delete old key
3. Create new key
4. Update `.env` file
5. Try again

### Fix 3: Check Model Availability
Make sure you're using an available model:
- ✅ `gpt-3.5-turbo` (cheapest, should work)
- ✅ `gpt-4` (more expensive, might need higher tier)
- ❌ Some models require specific account types

## 🎯 Most Likely Solution

**90% of the time, it's one of these:**

1. **Spending limit is $0** → Set it to $5+
2. **Credits are for ChatGPT Plus** → Add API credits separately
3. **Account needs payment method** → Add credit card (even with credits)

## 📞 Still Not Working?

1. **Check OpenAI Status:** https://status.openai.com
2. **Contact Support:** https://help.openai.com
3. **Check Account Email:** Make sure account is fully verified
4. **Try Different Model:** Use `gpt-3.5-turbo` (most compatible)

## ✅ Success Checklist

- [ ] Account has $5+ API credits (not just ChatGPT Plus)
- [ ] Payment method is added
- [ ] Spending limit is $5+ (not $0)
- [ ] API key is from same account
- [ ] Account is verified
- [ ] Using `gpt-3.5-turbo` model
- [ ] Test script works: `python test_api.py`

---

**The most common issue: Spending limit is set to $0 even though you have credits!**

