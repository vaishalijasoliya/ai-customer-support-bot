"""
Complete Setup Script - Run this to set up everything!
"""
import os
import subprocess
import sys

def create_env_file():
    """Create .env file with API key"""
    print("📝 Creating .env file...")
    env_content = """OPENAI_API_KEY=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
CHATBOT_NAME=SupportBot
COMPANY_NAME=Your Company
TEMPERATURE=0.7
MAX_TOKENS=500

# Test Mode - Set to true for FREE testing without API calls!
TEST_MODE=true
"""
    with open('.env', 'w') as f:
        f.write(env_content)
    print("✅ .env file created!")

def install_dependencies():
    """Install required packages"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def setup_knowledge_base():
    """Set up initial knowledge base"""
    print("\n📚 Setting up knowledge base...")
    try:
        subprocess.check_call([sys.executable, "setup_knowledge_base.py"])
        print("✅ Knowledge base set up!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Knowledge base setup had issues (this is okay): {e}")
        return True  # This is optional

def main():
    print("=" * 50)
    print("🚀 AI Customer Support Bot - Complete Setup")
    print("=" * 50)
    
    # Step 1: Create .env file
    create_env_file()
    
    # Step 2: Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed at dependency installation.")
        print("Please run manually: pip install -r requirements.txt")
        return
    
    # Step 3: Setup knowledge base
    setup_knowledge_base()
    
    print("\n" + "=" * 50)
    print("✅ SETUP COMPLETE!")
    print("=" * 50)
    print("\n🎉 Everything is ready!")
    print("\n📋 Next steps:")
    print("   1. Run: streamlit run app.py")
    print("   2. Your browser will open automatically")
    print("   3. Start chatting with your bot!")
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()

