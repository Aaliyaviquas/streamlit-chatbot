import streamlit as st
st.title("Streamlit Chatbot")
import os 
os.environ["GOOGLE_API_KEY"]=st.secrets["GOOGLE_API_KEY"]
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Streamlit page settings
st.set_page_config(page_title="Gemini Chat (LangChain)", layout="centered")
st.title("🤖 Gemini Chatbot")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Display existing messages
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        st.chat_message("user").markdown(message.content)
    elif isinstance(message, AIMessage):
        st.chat_message("assistant").markdown(message.content)

# User input
user_input = st.chat_input("Say something...")
if user_input:
    # Append user's message to history
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.chat_message("user").markdown(user_input)

    # Get LLM response using chat history
    with st.spinner("Thinking..."):
        result = llm.invoke(st.session_state.chat_history)

    # Append AI response to history
    ai_response = AIMessage(content=result.content)
    st.session_state.chat_history.append(ai_response)

    # Display AI response
    st.chat_message("assistant").markdown(result.content)
