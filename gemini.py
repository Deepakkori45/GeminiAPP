import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Page icon emoji
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
    # Assume this is the predefined user prompt (the user's input that's treated as part of the initial setup)
    predefined_user_prompt = "I want to improve my fitness routine."
    # Bot's first message asking how it can help, responding to the predefined user prompt
    bot_first_message = "How can I help you today?"
    # Add both messages to the chat history as if the conversation already started
    st.session_state.chat_session["history"].append({"role": "user", "text": predefined_user_prompt})
    st.session_state.chat_session["history"].append({"role": "model", "text": bot_first_message})

# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Display the chat history
for message in st.session_state.chat_session["history"]:
    with st.chat_message(translate_role_for_streamlit(message["role"])):
        st.markdown(message["text"])

# Input field for user's message
user_prompt = st.chat_input("Your response:")
if user_prompt:
    # This is the user's response to the bot's question
    st.session_state.chat_session["history"].append({"role": "user", "text": user_prompt})

    # Here you would normally send the user_prompt to the model and get a response
    # For demonstration, we simulate a model response
    gemini_response_text = "Simulated response based on your need for fitness routine improvement."

    # Add the model's simulated response to the chat history
    st.session_state.chat_session["history"].append({"role": "model", "text": gemini_response_text})

    # Optionally, display the model's response immediately
    with st.chat_message("assistant"):
        st.markdown(gemini_response_text)
