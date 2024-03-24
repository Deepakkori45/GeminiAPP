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

# Predefined conversations to be added into the chat history initially
predefined_conversations = [
    {"role": "user", "text": "This is a predefined user message that won't be displayed."},
    {"role": "model", "text": "This is a predefined model response that won't be displayed."}
]

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    # Start the chat session and include predefined conversations in the history
    st.session_state.chat_session = model.start_chat(history=predefined_conversations)
    # Additionally mark that the first real user message hasn't been sent yet
    st.session_state.first_message_sent = False

# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Display the chat history, skipping predefined conversations
for message in st.session_state.chat_session.history[2:]:  # Adjust index as needed based on predefined messages
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    if not st.session_state.first_message_sent:
        # Prepend the predefined prompt to the user's first message for model processing
        user_prompt_with_context = "Imagine me as your seasoned fitness guru... " + user_prompt
        # Mark the first real user message as sent
        st.session_state.first_message_sent = True
    else:
        # For subsequent messages, just use the user's input for model processing
        user_prompt_with_context = user_prompt

    # Send the modified or original user's message to Gemini-Pro and get the response
    gemini_response = model.send_message(user_prompt_with_context)  # Adjust this line based on the actual model interaction

    # Append the user's real message and the model's response to the chat history
    st.session_state.chat_session.history.append({"role": "user", "text": user_prompt})
    st.session_state.chat_session.history.append({"role": "model", "text": gemini_response.text})

    # Display the user's input and Gemini-Pro's response
    with st.chat_message("user"):
        st.markdown(user_prompt)
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
