import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.rag_chain import ask_question

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("🤖 RAG Chatbot")
st.write("Ask questions from your documents")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:")

if user_input:
    result = ask_question(user_input)

    answer = result["answer"]
    sources = result["source_documents"]

    st.session_state.chat.append((user_input, answer, sources))

for q, a, s in st.session_state.chat:
    st.markdown(f"**User:** {q}")
    st.markdown(f"**Bot:** {a}")

    if s:
        with st.expander("📄 Sources"):
            for doc in s:
                st.write(doc.metadata.get("source", "Unknown"))
