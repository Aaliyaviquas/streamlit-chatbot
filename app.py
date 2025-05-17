import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Initialize the language model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

# Streamlit app title
st.title("Chat with AI Assistant")

# Display chat history
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        st.write(f"**You**: {message.content}")
    elif isinstance(message, AIMessage):
        st.write(f"**AI**: {message.content}")

# User input
user_input = st.text_input("Your message:", key="user_input")

# Handle user input
if user_input:
    if user_input.lower() == "quit":
        st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]
        st.write("Chat ended. Session reset.")
    else:
        # Append user message to chat history
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        
        # Get AI response
        result = llm.invoke(st.session_state.chat_history)
        
        # Append AI response to chat history
        st.session_state.chat_history.append(AIMessage(content=result.content))
        
        # Refresh the page to show the new messages
        st.rerun()
