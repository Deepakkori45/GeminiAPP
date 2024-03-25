# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",  # Removed the non-breaking space
#     page_icon=":brain:",  # Favicon emoji
#     layout="centered",  # Page layout option
# )

# # Your Google API key
# GOOGLE_API_KEY = "AIzaSyC5jVGT9OHx4soEsliU60ByZsieobJPRms"

# # Set up Google Gemini-Pro AI model
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')

# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#   if user_role == "model":
#     return "assistant"
#   else:
#     return user_role

# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#   st.session_state.chat_session = model.start_chat(history=[])

# # Display the chatbot's title on the page
# st.title(" Gemini Pro - ChatBot")

# # Predefined prompt for the first message
# predefined_prompt = "Imagine me as your seasoned fitness guru, sculpting bodies like a potter shapes clay. I'll begin by molding your understanding with metaphors, guiding you through the intricacies of fitness like a dance instructor leads a beginner through steps. Then, once the metaphor paints the picture, I'll provide you with the straightforward, no-nonsense advice to help you achieve your fitness goals. So, let's take the first step together - what aspect of your fitness journey can I assist you with today?"

# # Display the chat history
# for message in st.session_state.chat_session.history:
#   with st.chat_message(translate_role_for_streamlit(message.role)):
#     st.markdown(message.parts[0].text)

# # Input field for user's message
# user_prompt = st.chat_input("Ask Gemini-Pro...")
# if user_prompt:
#   # Check if it's the first user's message in the session
#   if "first_message_sent" not in st.session_state:
#     # Prepend the predefined prompt to the user's first message for model processing
#     user_prompt_with_context = predefined_prompt + user_prompt
#     # Mark the first message as sent in the session state
#     st.session_state.first_message_sent = True
#   else:
#     # For subsequent messages, just use the user's input for model processing
#     user_prompt_with_context = user_prompt

#   # Always add user's original message to chat and display it
#   st.chat_message("user").markdown(user_prompt)

#   # Send the modified or original user's message to Gemini-Pro and get the response
#   gemini_response = st.session_state.chat_session.send_message(user_prompt_with_context)

#   # Display Gemini-Pro's response
#   with st.chat_message("assistant"):
#     st.markdown(gemini_response.text)

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import os

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",
    layout="centered",
)

# Your Google API key
GOOGLE_API_KEY = "AIzaSyC5jVGT9OHx4soEsliU60ByZsieobJPRms"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else "user"

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.displayed_messages = []

# Function to handle sending and displaying messages
def handle_message(user_prompt):
    # Preparing and sending the message
    response = st.session_state.chat_session.send_message(user_prompt)
    
    # Appending the user's message and model's response to the displayed messages list
    st.session_state.displayed_messages.append({
        "role": "user",
        "text": user_prompt
    })
    st.session_state.displayed_messages.append({
        "role": "assistant",
        "text": response.text
    })

    # Displaying messages from the displayed_messages list
    for message in st.session_state.displayed_messages:
        with st.chat_message(translate_role_for_streamlit(message["role"])):
            st.markdown(message["text"])

# Display the chatbot's title on the page
st.title("Gemini Pro - ChatBot")

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    # Check if it's the first user's message in the session
    if "first_message_sent" not in st.session_state:
        # Prepend a custom prompt to the user's first message
        user_prompt = "Your custom first message. " + user_prompt
        st.session_state.first_message_sent = True
    
    handle_message(user_prompt)

