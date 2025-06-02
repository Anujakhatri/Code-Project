import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",
    layout="centered",
)

# Safely load your actual API key from environment
GOOGLE_API_KEY = os.getenv("AIzaSyCuJiRvgOOYwT8-fhucbEBzTuArrB9h2Bs")  # Fix: load key by variable name, not raw value
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate Gemini roles to Streamlit chat message types
def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

# ✅ Initialize the chat session FIRST
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# ⬇️ Now that chat_session is initialized, you can display messages
st.title("🤖 Gemini Pro - ChatBot")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# User input
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
