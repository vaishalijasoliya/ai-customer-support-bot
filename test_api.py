"""
Test script to check OpenAI API connection and credits
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY", "")

if not api_key:
    print("❌ No API key found in .env file")
    exit(1)

print(f"✅ API Key found: {api_key[:20]}...")

# Initialize client
client = OpenAI(api_key=api_key)

print("\n🔍 Testing API connection...")

try:
    # Try a simple test call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Say 'Hello, API is working!'"}
        ],
        max_tokens=50
    )
    
    print("✅ API is working!")
    print(f"Response: {response.choices[0].message.content}")
    print(f"Model used: {response.model}")
    print(f"Tokens used: {response.usage.total_tokens}")
    
except Exception as e:
    error_str = str(e)
    print(f"\n❌ Error occurred:")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {error_str}")
    
    if "insufficient_quota" in error_str:
        print("\n💡 Possible issues:")
        print("1. Credits might be on a different account")
        print("2. API key might be from a different account")
        print("3. Account might need verification")
        print("4. Credits might be for ChatGPT Plus, not API")
        print("\nCheck: https://platform.openai.com/account/billing")
        
    elif "Invalid API key" in error_str or "401" in error_str:
        print("\n💡 API key is invalid or expired")
        print("Get a new key: https://platform.openai.com/api-keys")
        
    elif "rate_limit" in error_str.lower():
        print("\n💡 Rate limit - too many requests")
        print("Wait a few minutes and try again")
    
    else:
        print(f"\n💡 Unknown error - check OpenAI status: https://status.openai.com")

