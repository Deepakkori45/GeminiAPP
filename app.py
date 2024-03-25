import streamlit as st
import google.generativeai as gen_ai
from google.generativeai.types.generation_types import BlockedPromptException, StopCandidateException

# Configure Streamlit page settings
st.set_page_config(page_title="Chat with Gemini-Pro!", page_icon=":brain:", layout="centered")

# Your Google API key
GOOGLE_API_KEY = "AIzaSyC5jVGT9OHx4soEsliU60ByZsieobJPRms"  # Replace this with your real API key

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
  if user_role == "model":
    return "assistant"
  else:
    return user_role

def get_initial_prompt():
  """Provides the initial prompt for Gemini-Pro at session start."""
  return "Hi there! I'm Gemini-Pro, your friendly fitness guru. How can I help you today?"

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
  # Seed conversation history with initial prompt (hidden)
  initial_prompt = get_initial_prompt()
  st.session_state.chat_session = model.start_chat(history=[
      gen_ai.ChatMessage(role="user", parts=[gen_ai.TextPart(text=initial_prompt)])  # Hidden prompt
  ])

  # Generate response to initial prompt (hidden from user)
  response = st.session_state.chat_session.send_message(initial_prompt)

# Display the chatbot's title on the page
st.title(" Gemini Pro - ChatBot")

# Hide loop for displaying chat history (optional)
with st.expander("Chat History"):
  for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
      st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")

if user_prompt:
  # Add user's message to chat and display it
  st.chat_message("user").markdown(user_prompt)

  # Attempt to send user's message to Gemini-Pro and get the response
  gemini_response = st.session_state.chat_session.send_message(user_prompt)

  # Display Gemini-Pro's response
  with st.chat_message("assistant"):
    st.markdown(gemini_response.text)
