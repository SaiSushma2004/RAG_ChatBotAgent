# RAG_ChatBotAgent
# RAG Chatbot using LangChain, FAISS & Groq

## 📌 Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions based on their own documents. The system retrieves relevant information from uploaded files and generates accurate answers using a Large Language Model.
This project is built as a learning + portfolio-ready application for understanding modern GenAI architectures.


## 🚀Key Features
📄 Document-based Question Answering (RAG)
🔍 Semantic search using vector embeddings
🧠 Groq LLM integration
💬 Conversational memory
🖥️ Interactive Streamlit UI
📚 Source document citation
🛡️ Graceful fallback when information is not found

## 🛠 Tech Stack
Python 3.10+
Streamlit – frontend UI
LangChain – RAG pipeline
Groq LLM – text generation
ChromaDB – vector database
Sentence Transformers – embeddings
Hugging Face Models
dotenv – environment variables

## 📂 Project Structure

RAG_Agent/
│
├── backend/
│   ├── rag_chain.py          # RAG logic (retrieval + generation)
│   ├── vectorstore.py        # Vector DB creation & loading
│   ├── __init__.py
│
├── frontend/
│   ├── app.py                # Streamlit UI
│
├── data/
│   ├── ai.txt
│   ├── ml.txt
│   ├── rag.txt               # Knowledge source files
│
├── vectordb/                 # Auto-generated vector store
│
├── .env                      # API keys
├── requirements.txt
├── README.md
└── .gitignore

## 🔍 How RAG Works
1. Documents are loaded from the data/ folder
2. Text is split into chunks
3. Embeddings are created
4. Vectors are stored in ChromaDB
5. User asks a question via Streamlit UI
6. Relevant documents are retrieved
7. LLM generates an answer using retrieved context
8. If no relevant data is found → safe fallback message is shown

🚀 How to Run the Project Locally
## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone <repository-url>
cd RAG_Agent

2. Create Virtual Environment (Optional but Recommended)
python -m venv .venv
.venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Add Environment Variables
Create a .env file:
GROQ_API_KEY=your_groq_api_key_here

## ▶️ Run the Application
streamlit run frontend/app.py
Open browser at:
http://localhost:8501


🧠 LLM Model Used
Groq Model:llama-3.1-8b-instant (or any currently supported Groq model)
⚠️ Older models like llama3-8b-8192 are deprecated and will throw errors.

🗂️ Vector Database Behavior
Vector database is automatically created
Stored locally in vectordb/
If deleted, it will rebuild automatically on next run
No manual download required

❗ Fallback Behavior (Important)
If a question is not related to provided documents:
Response shown: I could not find relevant information in the provided documents.
This prevents hallucinations and improves trust.

📄 Source Document Display
Each answer includes:📄 Sources: dl.txt, ml.txt, rag.txt
This helps users verify where the answer came from.

🔒 Security Best Practices
API keys stored in .env
.gitignore blocks:
.env
.venv
vector DB
cache files

📈 Future Enhancements
🔹 Basic Level
Upload documents via UI
Clear chat history button
Dark/Light mode toggle

🔸 Intermediate Level
Multi-file upload (PDF, DOCX)
Metadata-based filtering
Answer confidence score
Chat history persistence

🔺 Advanced Level
User authentication
Multi-LLM support
Cloud vector DB (Pinecone / Weaviate)
Streaming responses
Production deployment (Docker)

🎯 Learning Outcomes

Understanding RAG architecture
Hands-on LangChain usage
Vector databases & embeddings
LLM API integration
Streamlit-based GenAI apps
Debugging real-world GenAI errors

