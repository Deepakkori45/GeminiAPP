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

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
  # Seed conversation history with desired user conversation (hidden)
  st.session_state.chat_session = model.start_chat(history=[
      gen_ai.ChatMessage(role="user", parts=[gen_ai.TextPart(text=prompt)])  # Don't display prompt in history
  ])

# Display the chatbot's title on the page
st.title(" Gemini Pro - ChatBot")

# Hide loop for displaying chat history
with st.expander("Chat History"):
  for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
      # Only display the message text, not model parts
      st.markdown(message.text)

prompt= "you are fitness guru."
# Send prompt to set Gemini-Pro in fitness guru mode (hidden from user)
st.session_state.chat_session.send_message(prompt)  # This doesn't need to be displayed

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")

if user_prompt:
  try:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Attempt to send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
      st.markdown(gemini_response.text)
  except Exception as e:
    # Handle any exception by logging and asking the user to try again
    # st.exception("An error occurred: {}".format(e))
    st.warning("Please try asking your question again.")
