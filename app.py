"""
Streamlit Web Interface for AI Customer Support Bot
"""
import streamlit as st
from chatbot import CustomerSupportBot
from config import CHATBOT_NAME, COMPANY_NAME, TEST_MODE
import json

# Page configuration
st.set_page_config(
    page_title=f"{CHATBOT_NAME} - Customer Support",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "bot" not in st.session_state:
    st.session_state.bot = CustomerSupportBot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .company-name {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stChatMessage {
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f'<div class="main-header">🤖 {CHATBOT_NAME}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="company-name">{COMPANY_NAME} Customer Support</div>', unsafe_allow_html=True)

# Show test mode indicator
if TEST_MODE:
    st.info("🧪 **TEST MODE ACTIVE** - No API calls, completely FREE! Responses are simulated.")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Knowledge Base Management
    st.subheader("📚 Knowledge Base")
    
    with st.expander("Add FAQ"):
        faq_question = st.text_input("Question:")
        faq_answer = st.text_area("Answer:")
        if st.button("Add FAQ"):
            if faq_question and faq_answer:
                st.session_state.bot.add_faq(faq_question, faq_answer)
                st.success("FAQ added successfully!")
    
    with st.expander("Add Document"):
        doc_content = st.text_area("Document Content:")
        if st.button("Add Document"):
            if doc_content:
                st.session_state.bot.add_knowledge(doc_content)
                st.success("Document added successfully!")
    
    # Reset conversation
    if st.button("🔄 Reset Conversation"):
        st.session_state.bot.reset_conversation()
        st.session_state.messages = []
        st.rerun()
    
    # Info
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.info(f"""
    This is an AI-powered customer support bot.
    
    **Features:**
    - 24/7 availability
    - Knowledge base integration
    - Context-aware responses
    - Multi-turn conversations
    """)

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
st.markdown(f"<div style='text-align: center; color: #666;'>Powered by AI • {COMPANY_NAME}</div>", unsafe_allow_html=True)


