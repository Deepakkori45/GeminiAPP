# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai

# # Load environment variables if necessary

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",
#     page_icon=":brain:",  # Favicon emoji
#     layout="centered",  # Page layout option
# )

# GOOGLE_API_KEY = "AIzaSyC5jVGT9OHx4soEsliU60ByZsieobJPRms"  # Replace this with your real API key

# # Set up Google Gemini-Pro AI model
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')

# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#     if user_role == "model":
#         return "assistant"
#     else:
#         return user_role

# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])

# # Display the chatbot's title on the page
# st.title("🤖 Gemini Pro - ChatBot")

# # Display the chat history
# for message in st.session_state.chat_session.history:
#     with st.chat_message(translate_role_for_streamlit(message.role)):
#         st.markdown(message.parts[0].text)

# # Input field for user's message
# user_prompt = st.chat_input("Ask Gemini-Pro...")
# if user_prompt:
#     # Add user's message to chat and display it
#     st.chat_message("user").markdown(user_prompt)

#     # Send user's message to Gemini-Pro and get the response
#     gemini_response = st.session_state.chat_session.send_message(user_prompt)

#     # Display Gemini-Pro's response
#     with st.chat_message("assistant"):
#         st.markdown(gemini_response.text)

# # Add a comment here to describe your web app code
# # This is a Streamlit app that integrates Google Gemini-Pro AI model for chat interactions.
# # It displays a chat interface where users can converse with the Gemini-Pro assistant.
# # User messages are sent to the AI model, and responses are displayed back to the user.
# # The chat history is maintained and displayed in the app interface.
import google.generativeai as gen_ai

# Your Google API key
GOOGLE_API_KEY = "AIzaSyC5jVGT9OHx4soEsliU60ByZsieobJPRms"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to handle the conversation
def chat_with_gemini():
    print("Gemini: Hi! I'm Gemini, your virtual assistant. How can I assist you today?")
    print("(Type 'exit' to end the conversation)")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Gemini: Goodbye! Have a great day.")
            break

        try:
            # Send the user's message to Gemini and get the response
            gemini_response = model.chat(user_input)
            print("Gemini:", gemini_response.text)
        except gen_ai.types.generation_types.StopCandidateException:
            print("Gemini: Can you write again? I did not understand.")

# Initiate the conversation
chat_with_gemini()
