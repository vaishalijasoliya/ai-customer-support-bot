"""
Main Chatbot Engine
"""
from typing import List, Dict
from openai import OpenAI
from config import (
    OPENAI_API_KEY, 
    OPENAI_MODEL, 
    SYSTEM_PROMPT, 
    TEMPERATURE, 
    MAX_TOKENS,
    TEST_MODE
)
from knowledge_base_manager import KnowledgeBaseManager

class CustomerSupportBot:
    def __init__(self):
        self.test_mode = TEST_MODE
        if not self.test_mode:
            self.client = OpenAI(api_key=OPENAI_API_KEY)
        else:
            self.client = None
            print("🧪 TEST MODE ENABLED - No API calls will be made (FREE testing!)")
        self.knowledge_base = KnowledgeBaseManager()
        self.conversation_history: List[Dict] = []
    
    def _generate_mock_response(self, user_message: str, context: str = "") -> str:
        """
        Generate a mock response for testing without API calls
        This simulates AI responses based on keywords and knowledge base
        """
        user_lower = user_message.lower()
        
        # Check knowledge base first
        if context:
            # If we have context, use it
            return f"""Thank you for your question! Based on our knowledge base:

{context}

I hope this helps! Is there anything else I can assist you with?"""
        
        # Keyword-based responses (simulating AI)
        responses = {
            "hello": "Hello! I'm here to help you. How can I assist you today?",
            "hi": "Hi there! Welcome to our customer support. What can I help you with?",
            "help": "I'm here to help! Please let me know what you need assistance with.",
            "hours": "Our business hours are Monday through Friday, 9 AM to 6 PM EST. For urgent matters, you can reach us via email.",
            "order": "To track your order, please log into your account and go to the 'My Orders' section. You'll receive tracking information via email once your order ships.",
            "return": "We offer a 30-day return policy on all products. Items must be in original condition with tags attached. Please contact our support team to initiate a return.",
            "contact": "You can reach our customer support team via email at support@company.com, through this chat, or by calling 1-800-SUPPORT. We're here to help!",
            "shipping": "Yes, we ship internationally to over 50 countries. Shipping costs and delivery times vary by location. You can check shipping options during checkout.",
            "price": "For pricing information, please visit our website or contact our sales team. We'd be happy to provide you with a quote!",
            "payment": "We accept all major credit cards, PayPal, and bank transfers. Payment is processed securely at checkout.",
        }
        
        # Check for keywords
        for keyword, response in responses.items():
            if keyword in user_lower:
                return response
        
        # Default response
        return f"""Thank you for contacting us! I understand you're asking about: "{user_message}"

I'm currently in TEST MODE (no API costs), so I'm providing a simulated response. 

In production mode with a valid API key, I would provide a detailed, AI-powered answer based on your question and our knowledge base.

Is there anything specific I can help you with? Feel free to ask about:
- Business hours
- Order tracking
- Returns and refunds
- Shipping information
- Payment methods
- Or any other questions!"""
    
    def get_response(self, user_message: str, use_knowledge_base: bool = True) -> str:
        """
        Get response from the chatbot
        
        Args:
            user_message: The user's message
            use_knowledge_base: Whether to use knowledge base for context
        
        Returns:
            The chatbot's response
        """
        # Get relevant context from knowledge base
        context = ""
        if use_knowledge_base:
            context = self.knowledge_base.get_context(user_message)
        
        # Build the prompt with context
        if context:
            enhanced_prompt = f"""Use the following information to answer the customer's question. If the information doesn't contain the answer, use your general knowledge but be honest if you're uncertain.

Context from knowledge base:
{context}

Customer question: {user_message}

Provide a helpful, professional response:"""
        else:
            enhanced_prompt = user_message
        
        # Add to conversation history
        self.conversation_history.append({"role": "user", "content": user_message})
        
        # Prepare messages
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        
        # Add recent conversation history (last 5 exchanges to manage token usage)
        recent_history = self.conversation_history[-10:] if len(self.conversation_history) > 10 else self.conversation_history
        messages.extend(recent_history)
        
        # Add current user message
        messages.append({"role": "user", "content": enhanced_prompt})
        
        # TEST MODE: Use mock responses (FREE, no API calls!)
        if self.test_mode:
            bot_response = self._generate_mock_response(user_message, context)
            self.conversation_history.append({"role": "assistant", "content": bot_response})
            return bot_response
        
        # PRODUCTION MODE: Use real OpenAI API
        try:
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=messages,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS
            )
            
            bot_response = response.choices[0].message.content
            
            # Add bot response to history
            self.conversation_history.append({"role": "assistant", "content": bot_response})
            
            return bot_response
        
        except Exception as e:
            error_str = str(e)
            
            # Handle specific OpenAI errors with user-friendly messages
            if "insufficient_quota" in error_str or "429" in error_str:
                return """⚠️ **API Quota Exceeded**

Your OpenAI account has run out of credits or doesn't have billing set up.

**To fix this:**
1. Go to https://platform.openai.com/account/billing
2. Add a payment method
3. Add credits to your account (minimum $5)
4. Or check if you've used all your free tier credits

**For testing:** You can use OpenAI's free tier credits when you first sign up, but they're limited.

**Note:** This is an account/billing issue, not a code problem. The bot code is working correctly."""
            
            elif "Invalid API key" in error_str or "401" in error_str:
                return """🔑 **Invalid API Key**

Your OpenAI API key is invalid or expired.

**To fix this:**
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Update the key in your `.env` file"""
            
            elif "rate_limit" in error_str.lower():
                return """⏱️ **Rate Limit Exceeded**

You're making too many requests too quickly.

**To fix this:**
- Wait a few minutes and try again
- Or upgrade your OpenAI plan for higher rate limits"""
            
            else:
                return f"""⚠️ **Technical Issue**

I'm experiencing a technical problem. Please try again.

**Error details:** {error_str}

If this persists, please check:
- Your internet connection
- OpenAI service status: https://status.openai.com
- Your API key is valid"""
    
    def reset_conversation(self):
        """Reset the conversation history"""
        self.conversation_history = []
    
    def add_knowledge(self, content: str, metadata: Dict = None):
        """Add knowledge to the knowledge base"""
        self.knowledge_base.add_document(content, metadata)
    
    def add_faq(self, question: str, answer: str):
        """Add a FAQ to the knowledge base"""
        self.knowledge_base.add_faq(question, answer)


