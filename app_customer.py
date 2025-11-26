"""
Customer-Facing Chat Interface
Clean interface for end users - NO admin features
"""
import streamlit as st
from chatbot import CustomerSupportBot
from config import CHATBOT_NAME, COMPANY_NAME, TEST_MODE

# Page configuration
st.set_page_config(
    page_title=f"{CHATBOT_NAME} - Customer Support",
    page_icon="🤖",
    layout="centered"  # Centered layout for customer view
)

# Initialize session state
if "bot" not in st.session_state:
    st.session_state.bot = CustomerSupportBot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom CSS for clean customer interface
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .company-name {
        font-size: 1.1rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stChatMessage {
        padding: 1rem;
    }
    /* Hide Streamlit menu and footer for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header - Clean and simple
st.markdown(f'<div class="main-header">🤖 {CHATBOT_NAME}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="company-name">{COMPANY_NAME} Customer Support</div>', unsafe_allow_html=True)

# Optional: Show test mode indicator (can be removed in production)
if TEST_MODE:
    st.info("🧪 **TEST MODE** - Simulated responses")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.bot.get_response(prompt)
            st.markdown(response)
    
    # Add bot response to chat
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: #666; font-size: 0.9rem;'>Powered by AI • {COMPANY_NAME}</div>", unsafe_allow_html=True)

