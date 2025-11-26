"""
Example: How to integrate the chatbot into your own application
"""
from chatbot import CustomerSupportBot

# Initialize the bot
bot = CustomerSupportBot()

# Example 1: Simple question-answer
def simple_chat():
    """Simple chat example"""
    user_message = "What are your business hours?"
    response = bot.get_response(user_message)
    print(f"User: {user_message}")
    print(f"Bot: {response}")

# Example 2: Multi-turn conversation
def multi_turn_chat():
    """Multi-turn conversation example"""
    messages = [
        "What is your return policy?",
        "How long does it take?",
        "Can I return items purchased online?"
    ]
    
    for message in messages:
        response = bot.get_response(message)
        print(f"\nUser: {message}")
        print(f"Bot: {response}")

# Example 3: Add custom knowledge
def setup_custom_knowledge():
    """Add custom knowledge for a specific client"""
    bot = CustomerSupportBot()
    
    # Add client-specific FAQs
    bot.add_faq(
        "What payment methods do you accept?",
        "We accept all major credit cards, PayPal, and bank transfers."
    )
    
    bot.add_faq(
        "Do you offer discounts?",
        "Yes! We offer a 10% discount for first-time customers. Use code WELCOME10 at checkout."
    )
    
    # Add product information
    product_info = """
    Our flagship product is the AI Assistant Pro, which includes:
    - 24/7 customer support
    - Multi-language support
    - CRM integration
    - Analytics dashboard
    
    Pricing: $99/month for basic plan, $199/month for professional plan.
    """
    bot.add_knowledge(product_info, metadata={"type": "product_info"})
    
    print("Custom knowledge added successfully!")

# Example 4: API endpoint (for web integration)
def api_endpoint_example():
    """
    Example of how to create an API endpoint
    This can be used with Flask, FastAPI, etc.
    """
    from flask import Flask, request, jsonify
    
    app = Flask(__name__)
    bot = CustomerSupportBot()
    
    @app.route('/chat', methods=['POST'])
    def chat():
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        response = bot.get_response(user_message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
    
    # Run: app.run(host='0.0.0.0', port=5000)
    return app

# Example 5: WhatsApp integration (conceptual)
def whatsapp_integration_example():
    """
    Example structure for WhatsApp integration
    You would use Twilio or WhatsApp Business API
    """
    from twilio.rest import Client
    
    # Initialize Twilio client (you'd get these from Twilio)
    # account_sid = "your_account_sid"
    # auth_token = "your_auth_token"
    # client = Client(account_sid, auth_token)
    
    bot = CustomerSupportBot()
    
    def handle_whatsapp_message(from_number, message_body):
        """Handle incoming WhatsApp message"""
        # Get bot response
        response = bot.get_response(message_body)
        
        # Send response via Twilio
        # message = client.messages.create(
        #     body=response,
        #     from_='whatsapp:+14155238886',
        #     to=f'whatsapp:{from_number}'
        # )
        
        return response
    
    return handle_whatsapp_message

if __name__ == "__main__":
    print("=== Example 1: Simple Chat ===")
    simple_chat()
    
    print("\n=== Example 2: Multi-turn Chat ===")
    multi_turn_chat()
    
    print("\n=== Example 3: Custom Knowledge ===")
    setup_custom_knowledge()


