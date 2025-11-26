"""
Script to set up initial knowledge base with sample FAQs
"""
from chatbot import CustomerSupportBot
from config import COMPANY_NAME

def setup_sample_knowledge_base():
    """Add sample FAQs and knowledge to the bot"""
    bot = CustomerSupportBot()
    
    print(f"Setting up knowledge base for {COMPANY_NAME}...")
    
    # Sample FAQs - customize these for your client
    sample_faqs = [
        {
            "question": "What are your business hours?",
            "answer": "We are open Monday through Friday from 9 AM to 6 PM EST. For urgent matters, you can reach us via email and we'll respond within 24 hours."
        },
        {
            "question": "How can I track my order?",
            "answer": "You can track your order by logging into your account and going to the 'My Orders' section. You'll receive tracking information via email once your order ships."
        },
        {
            "question": "What is your return policy?",
            "answer": "We offer a 30-day return policy on all products. Items must be in original condition with tags attached. Please contact our support team to initiate a return."
        },
        {
            "question": "How do I contact customer support?",
            "answer": "You can reach our customer support team via email at support@company.com, through this chat, or by calling 1-800-SUPPORT. We're here to help!"
        },
        {
            "question": "Do you offer international shipping?",
            "answer": "Yes, we ship internationally to over 50 countries. Shipping costs and delivery times vary by location. You can check shipping options during checkout."
        }
    ]
    
    # Add FAQs
    for faq in sample_faqs:
        bot.add_faq(faq["question"], faq["answer"])
        print(f"✓ Added FAQ: {faq['question']}")
    
    # Add general company information
    company_info = f"""
    About {COMPANY_NAME}:
    We are a customer-focused company dedicated to providing excellent products and services.
    Our mission is to deliver exceptional value to our customers while maintaining the highest standards of quality.
    
    Key Services:
    - Product sales and support
    - Technical assistance
    - Order management
    - Customer service
    
    We value our customers and are committed to providing the best possible experience.
    """
    
    bot.add_knowledge(company_info, metadata={"type": "company_info"})
    print("✓ Added company information")
    
    print("\n✅ Knowledge base setup complete!")
    print(f"Total FAQs added: {len(sample_faqs)}")
    print("\nYou can now run the chatbot with: streamlit run app.py")

if __name__ == "__main__":
    setup_sample_knowledge_base()


