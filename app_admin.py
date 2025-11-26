"""
Admin Panel - For Managing the Chatbot
Only admins should access this interface
"""
import streamlit as st
from chatbot import CustomerSupportBot
from config import CHATBOT_NAME, COMPANY_NAME, TEST_MODE
import os

# Page configuration
st.set_page_config(
    page_title=f"Admin Panel - {CHATBOT_NAME}",
    page_icon="⚙️",
    layout="wide"
)

# Simple password protection (for production, use proper authentication)
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")  # Change this!

# Check if user is authenticated
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Login page
if not st.session_state.authenticated:
    st.title("🔐 Admin Login")
    st.markdown("---")
    
    password = st.text_input("Enter Admin Password:", type="password")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Login"):
            if password == ADMIN_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Incorrect password!")
    
    st.info("💡 **Note:** Change ADMIN_PASSWORD in your environment variables for production!")
    st.stop()

# Admin Panel (only shown after login)
st.title(f"⚙️ Admin Panel - {CHATBOT_NAME}")
st.markdown(f"**Company:** {COMPANY_NAME}")

if TEST_MODE:
    st.warning("🧪 **TEST MODE ACTIVE** - No API calls are being made")

# Initialize bot
if "bot" not in st.session_state:
    st.session_state.bot = CustomerSupportBot()

# Tabs for different admin functions
tab1, tab2, tab3, tab4 = st.tabs(["📚 Knowledge Base", "💬 Test Chat", "📊 Analytics", "⚙️ Settings"])

# Tab 1: Knowledge Base Management
with tab1:
    st.header("📚 Knowledge Base Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Add FAQ")
        faq_question = st.text_input("Question:", key="faq_q")
        faq_answer = st.text_area("Answer:", height=150, key="faq_a")
        if st.button("➕ Add FAQ", type="primary"):
            if faq_question and faq_answer:
                st.session_state.bot.add_faq(faq_question, faq_answer)
                st.success("✅ FAQ added successfully!")
            else:
                st.error("Please fill in both question and answer")
    
    with col2:
        st.subheader("Add Document")
        doc_content = st.text_area("Document Content:", height=200, key="doc_content")
        doc_metadata = st.text_input("Metadata (optional, e.g., 'product_info'):", key="doc_meta")
        if st.button("➕ Add Document", type="primary"):
            if doc_content:
                metadata = {"type": doc_metadata} if doc_metadata else None
                st.session_state.bot.add_knowledge(doc_content, metadata)
                st.success("✅ Document added successfully!")
            else:
                st.error("Please enter document content")
    
    st.markdown("---")
    st.subheader("📋 Current Knowledge Base")
    
    # Show knowledge base stats
    if hasattr(st.session_state.bot.knowledge_base, 'simple_storage'):
        kb_count = len(st.session_state.bot.knowledge_base.simple_storage)
        st.info(f"📊 **Total items in knowledge base:** {kb_count}")
    else:
        st.info("📊 Knowledge base uses vector storage (check vector_store directory)")

# Tab 2: Test Chat
with tab2:
    st.header("💬 Test Chat Interface")
    st.info("Use this to test how the bot responds to customers")
    
    # Initialize test chat messages
    if "admin_messages" not in st.session_state:
        st.session_state.admin_messages = []
    
    # Display test chat history
    for message in st.session_state.admin_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Test chat input
    if test_prompt := st.chat_input("Test message..."):
        st.session_state.admin_messages.append({"role": "user", "content": test_prompt})
        with st.chat_message("user"):
            st.markdown(test_prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.bot.get_response(test_prompt)
                st.markdown(response)
        
        st.session_state.admin_messages.append({"role": "assistant", "content": response})
    
    if st.button("🔄 Clear Test Chat"):
        st.session_state.admin_messages = []
        st.session_state.bot.reset_conversation()
        st.rerun()

# Tab 3: Analytics
with tab3:
    st.header("📊 Analytics & Insights")
    
    st.info("📈 Analytics features coming soon!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Conversations", "N/A", "Coming soon")
    
    with col2:
        st.metric("Messages Handled", "N/A", "Coming soon")
    
    with col3:
        st.metric("Success Rate", "N/A", "Coming soon")
    
    st.markdown("---")
    st.subheader("💡 Future Analytics Features:")
    st.markdown("""
    - Total conversations
    - Most common questions
    - Response accuracy
    - Customer satisfaction
    - Peak usage times
    - Knowledge base effectiveness
    """)

# Tab 4: Settings
with tab4:
    st.header("⚙️ Settings")
    
    st.subheader("Bot Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"**Bot Name:** {CHATBOT_NAME}")
        st.info(f"**Company:** {COMPANY_NAME}")
        st.info(f"**Test Mode:** {'✅ Active' if TEST_MODE else '❌ Inactive'}")
    
    with col2:
        st.info("**Model:** GPT-3.5-turbo (default)")
        st.info("**Status:** 🟢 Online")
    
    st.markdown("---")
    st.subheader("⚠️ Danger Zone")
    
    if st.button("🗑️ Clear All Knowledge Base", type="secondary"):
        if st.checkbox("I understand this will delete all FAQs and documents"):
            st.session_state.bot.knowledge_base.clear_knowledge_base()
            st.error("🗑️ Knowledge base cleared!")
    
    st.markdown("---")
    st.subheader("🔐 Security")
    st.warning("💡 **Important:** Change ADMIN_PASSWORD in your `.env` file for production!")
    
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()

# Sidebar info
with st.sidebar:
    st.header("ℹ️ Admin Info")
    st.info(f"""
    **Bot:** {CHATBOT_NAME}
    **Company:** {COMPANY_NAME}
    **Mode:** {'🧪 Test' if TEST_MODE else '🚀 Production'}
    """)
    
    st.markdown("---")
    st.markdown("### 📖 Quick Links")
    st.markdown("""
    - [Customer Interface](http://localhost:8501)
    - [OpenAI Dashboard](https://platform.openai.com)
    - [Documentation](./README.md)
    """)

