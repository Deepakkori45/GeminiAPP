import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Your Google API key
GOOGLE_API_KEY = "AIzaSyC5jVGT9OHx4soEsliU60ByZsieobJPRms"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = {"history": []}
    # Add an initial message from the bot as part of the chat session initialization
    initial_bot_message = "How can I assist you with your fitness journey today?"
    st.session_state.chat_session["history"].append({"role": "model", "text": initial_bot_message})

# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Predefined prompt for the first message (background context)
predefined_prompt = "Imagine me as your seasoned fitness guru... [remainder of the predefined prompt]"

# Display the chat history
for message in st.session_state.chat_session["history"]:
    with st.chat_message(translate_role_for_streamlit(message["role"])):
        st.markdown(message["text"])

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    # Check if it's the first user's message in the session
    first_user_message = len([m for m in st.session_state.chat_session["history"] if m["role"] == "user"]) == 0
    if first_user_message:
        # Use the predefined prompt as background context for processing the first user message
        user_prompt_with_context = predefined_prompt + " " + user_prompt
    else:
        # For subsequent messages, just use the user's input
        user_prompt_with_context = user_prompt

    # Add the user's original message to the chat history
    st.session_state.chat_session["history"].append({"role": "user", "text": user_prompt})

    # Simulate sending the message (with context if first message) to the model and getting a response
    # For demonstration, replace this with actual model interaction
    gemini_response_text = "Simulated response based on: " + user_prompt_with_context

    # Add the model's response to the chat history
    st.session_state.chat_session["history"].append({"role": "model", "text": gemini_response_text})

    # Display the simulated model's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response_text)
