from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from backend.vectorstore import get_vectorstore
import os
from dotenv import load_dotenv

load_dotenv()

def ask_question(question: str):
    vectorstore = get_vectorstore()

    llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",

    temperature=0
)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

      # ✅ CUSTOM PROMPT
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a helpful AI assistant.
Answer the question strictly using the provided context.

If the answer is NOT present in the context, respond with:
"I could not find relevant information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
    )

    result = qa_chain({"question": question})


    return result
