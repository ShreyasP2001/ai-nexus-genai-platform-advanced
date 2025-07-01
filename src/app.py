import streamlit as st
from src.utils import load_environment
from src.user_auth import login_form
from src.rag_pipeline import rag_chat_interface
from src.forecast import forecast_interface
from src.pdf_parser import pdf_chat_interface
from src.tts_whisper import transcribe_audio

# Load environment variables (.env)
load_environment()

# Sidebar Navigation
st.sidebar.title("🧠 AI Nexus – Menu")
page = st.sidebar.radio("Select a module:", [
    "Login",
    "Chat with Documents (RAG)",
    "Forecasting",
    "PDF Intelligence",
    "Voice Transcription"
])

# Require login for all features
if not login_form():
    st.stop()

# Route based on selection
if page == "Chat with Documents (RAG)":
    rag_chat_interface()

elif page == "Forecasting":
    forecast_interface()

elif page == "PDF Intelligence":
    pdf_chat_interface()

elif page == "Voice Transcription":
    transcribe_audio()

# Footer
st.markdown("---")
st.markdown("© 2025 AI Nexus – Powered by Agentic & Generative AI")
