import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Streamlit page settings
st.set_page_config(page_title="Gemini Chat", layout="centered")
st.title("🤖 Popsicleco Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Display chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").markdown(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").markdown(msg.content)

# Input box
user_input = st.chat_input("Say something...")

# Handle new input
if user_input:
    # Append and display user message
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.chat_message("user").markdown(user_input)

    # Get AI response
    with st.spinner("Thinking..."):
        result = llm.invoke(st.session_state.chat_history)

    # Append and display AI message
    ai_response = AIMessage(content=result.content)
    st.session_state.chat_history.append(ai_response)
    st.chat_message("assistant").markdown(result.content)

# Optional: Reset button
if st.button("🔁 Reset Chat"):
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]
    st.rerun()
