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
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Predefined prompt for the first message
predefined_prompt = "Imagine me as your seasoned fitness guru... [remainder of the prompt]"

# Display the chat history
for message in st.session_state.chat_session.history:
    # Ensure only the original user message or model responses are displayed
    with st.chat_message(translate_role_for_streamlit(message['role'])):
        st.markdown(message['text'])

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    # Always add the user's original message to chat and display it
    # This is where you append the user message to the history
    st.session_state.chat_session.history.append({"role": "user", "text": user_prompt})

    # Determine if it's the first user message for the session
    first_user_message = len([m for m in st.session_state.chat_session.history if m['role'] == 'user']) == 1

    if first_user_message:
        # For the first message, prepend the predefined prompt for processing
        user_prompt_with_context = predefined_prompt + user_prompt
    else:
        # For subsequent messages, just use the user's input
        user_prompt_with_context = user_prompt

    # Send the user's message (or the modified first message) to the model
    # Assuming a function `send_to_model` sends the message to your model and returns the response
    # gemini_response = send_to_model(user_prompt_with_context)

    # Simulate receiving a response from the model
    gemini_response_text = "Simulated response based on: " + user_prompt_with_context

    # Add the model's response to the chat history
    st.session_state.chat_session.history.append({"role": "model", "text": gemini_response_text})

    # Optionally display the model's response immediately
    with st.chat_message("assistant"):
        st.markdown(gemini_response_text)
