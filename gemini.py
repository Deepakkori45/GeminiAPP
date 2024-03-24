import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(page_title="Chat with Gemini-Pro!", page_icon=":brain:", layout="centered")

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
    # Simulate the bot's initial message/question as part of the session initialization
    st.session_state.chat_session.history.append({"role": "model", "text": "How can I assist you today?"})

# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Predefined prompt for the first message
predefined_prompt = "Imagine me as your seasoned fitness guru... [your complete predefined prompt here]"

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    # Add user's original message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_session.history.append({"role": "user", "text": user_prompt})

    # Check if it's the first user's message in the session for processing
    if len([msg for msg in st.session_state.chat_session.history if msg["role"] == "user"]) == 1:
        # Only for the model processing, prepend the predefined prompt to the first user message
        user_prompt_with_context = predefined_prompt + user_prompt
    else:
        # For subsequent messages, just use the user's input for model processing
        user_prompt_with_context = user_prompt

    # Send the user's message to Gemini-Pro and get the response (simulated here)
    # gemini_response = model.send_message(user_prompt_with_context)
    # For demonstration, we simulate appending a model-generated message
    st.session_state.chat_session.history.append({"role": "model", "text": "Simulated response based on: " + user_prompt_with_context})

    # Display the simulated Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown("Simulated response based on: " + user_prompt_with_context)
