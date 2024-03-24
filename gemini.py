import streamlit as st
# from dotenv import load_dotenv  # Uncomment if dotenv is used for other purposes
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
predefined_prompt = "Imagine me as your seasoned fitness guru, sculpting bodies like a potter shapes clay..."

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message['role'])):  # Adjusted to use dictionary key access
        st.markdown(message['text'])  # Adjusted to use dictionary key access

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    if "first_message_sent" not in st.session_state:
        # Prepend the predefined prompt to the user's first message for model processing
        user_prompt_with_context = predefined_prompt + user_prompt
        st.session_state.first_message_sent = True  # Mark the first message as sent
    else:
        user_prompt_with_context = user_prompt  # For subsequent messages

    # Send the modified or original user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt_with_context)

    # Handling response assuming 'gemini_response' contains directly accessible text
    if hasattr(gemini_response, 'text'):  # Directly using the 'text' attribute
        response_text = gemini_response.text
    else:
        response_text = "Unexpected response format from the model."

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(response_text)
