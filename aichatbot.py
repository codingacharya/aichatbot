import streamlit as st
import openai

# Streamlit UI
st.title("Chatbot with OpenAI API")

# Input for API key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me anything!")
if user_input and api_key:
    # Append user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Call OpenAI API
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state.messages
    )
    
    bot_reply = response["choices"][0]["message"]["content"]
    
    # Append bot message to history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
