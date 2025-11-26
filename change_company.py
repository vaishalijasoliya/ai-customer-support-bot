"""
Quick script to change company name and chatbot name
Usage: python change_company.py "Company Name" [Bot Name]
"""
import sys
import os

def update_env_file(company_name, bot_name=None):
    """Update .env file with new company name"""
    env_file = '.env'
    
    if not os.path.exists(env_file):
        print("❌ .env file not found!")
        print("Creating new .env file...")
        # Create basic .env file
        with open(env_file, 'w') as f:
            f.write(f"""OPENAI_API_KEY=your_api_key_here
CHATBOT_NAME=SupportBot
COMPANY_NAME={company_name}
TEMPERATURE=0.7
MAX_TOKENS=500
TEST_MODE=true
""")
        print(f"✅ Created .env file with COMPANY_NAME={company_name}")
        return
    
    # Read existing .env file
    with open(env_file, 'r') as f:
        lines = f.readlines()
    
    # Update COMPANY_NAME
    updated = False
    new_lines = []
    for line in lines:
        if line.startswith('COMPANY_NAME='):
            new_lines.append(f'COMPANY_NAME={company_name}\n')
            updated = True
        elif bot_name and line.startswith('CHATBOT_NAME='):
            new_lines.append(f'CHATBOT_NAME={bot_name}\n')
        else:
            new_lines.append(line)
    
    # If COMPANY_NAME wasn't found, add it
    if not updated:
        new_lines.append(f'COMPANY_NAME={company_name}\n')
    
    # Write back to file
    with open(env_file, 'w') as f:
        f.writelines(new_lines)
    
    print(f"✅ Updated COMPANY_NAME to: {company_name}")
    if bot_name:
        print(f"✅ Updated CHATBOT_NAME to: {bot_name}")
    print("\n💡 Restart your Streamlit app to see changes!")

def main():
    if len(sys.argv) < 2:
        print("Usage: python change_company.py 'Company Name' [Bot Name]")
        print("\nExample:")
        print("  python change_company.py 'Acme Corporation'")
        print("  python change_company.py 'Acme Corporation' 'Alex'")
        return
    
    company_name = sys.argv[1]
    bot_name = sys.argv[2] if len(sys.argv) > 2 else None
    
    update_env_file(company_name, bot_name)

if __name__ == "__main__":
    main()

