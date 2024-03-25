# Import the necessary libraries
from openai import OpenAI
import streamlit as st

# Set the title of the Streamlit web application
st.title("ChatGPT-like clone")

# Initialize the OpenAI client with the API key stored in Streamlit secrets
# This requires having an `OPENAI_API_KEY` set up in your Streamlit secrets configuration
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Check if the model name is not already stored in session_state, then initialize it
# This sets the default model to use for generating responses
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Check if the messages list is not already stored in session_state, then initialize it
# This will store the conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Loop through the stored messages and display them in the UI
# This reconstructs the chat history on the page
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create an input box for the user to type their message
# `st.chat_input` creates a styled chat input box
if prompt := st.chat_input("What is up?"):
    # Append the user's message to the session_state messages list
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display the user's message using the chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a response from the OpenAI API
    # The API call includes specifying the model and passing the current conversation history
    # The 'stream=True' argument allows for streaming the API response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ) 
        # Write the API's stream response to the chat
        response = st.write_stream(stream)

    # Append the assistant's response to the session_state messages list
    st.session_state.messages.append({"role": "assistant", "content": response})

# The last part (starting from "# Display assistant response in chat message container") seems to be a repetition
# of the assistant response generation code block above. It likely doesn't need to be repeated and can be removed.
