import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Baby Bliss!",
    page_icon=":baby:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Your Google API key
GOOGLE_API_KEY = "AIzaSyAq0fyDOUvYGeKzFWB15LvCIL4T7ujIOm0"

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
st.title("👶 Baby Bliss Massage Bot")

# Predefined prompt for the first message
predefined_prompt = """ Response only what user asks you in short.
You are a knowledgeable therapist specializing in baby massage at Baby Bliss Therapy Center. With over a decade of experience, you provide educational information and personalized consultation to parents and caregivers about the benefits and techniques of baby massage. Your role is to support new parents by sharing insights on how baby massage can aid in their child's development and improve overall health. Please respond to queries with direct information and professional advice, citing current practices and research when possible.
Your task is to provide detailed, accurate responses that educate parents on the advantages of baby massage and encourage them to book a session with us.
Start with this "Hi there, I'm your friendly Baby Bliss Massage Bot. How can I assist you with your today?" """

# Display the chat history
count = 0
for message in st.session_state.chat_session.history:
    if count == 0:
        st.markdown(" ")
        count += 1
    else:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Baby Bliss...")

if user_prompt:
    try:
        # Check if it's the first user's message in the session
        if "first_message_sent" not in st.session_state:
            # Prepend the predefined prompt to the user's first message for model processing
            user_prompt_with_context = predefined_prompt + user_prompt
            # Mark the first message as sent in the session state
            st.session_state.first_message_sent = True
        else:
            # For subsequent messages, just use the user's input for model processing
            user_prompt_with_context = user_prompt

        # Always add user's original message to chat and display it
        st.chat_message("user").markdown(user_prompt)

        # Send the modified or original user's message to Gemini-Pro and get the response
        gemini_response = st.session_state.chat_session.send_message(user_prompt_with_context)

        # Display Gemini-Pro's response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
    except Exception as e:
        # Handle any exception by logging and asking the user to try again
        st.warning("Please try asking your question again.")
