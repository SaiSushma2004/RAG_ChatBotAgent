import sys
import os
import streamlit as st

# Allow Streamlit to find backend package
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from backend.rag_chain import ask_question

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("🤖 RAG Chatbot")
st.write("Ask questions from your documents")

# Session state for chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:")

if user_input:
    # Backend returns ONLY a string
    answer = ask_question(user_input)

    # Store question + answer
    st.session_state.chat.append((user_input, answer))

# Display chat history
for q, a in st.session_state.chat:
    st.markdown(f"**User:** {q}")
    st.markdown(f"**Bot:** {a}")
