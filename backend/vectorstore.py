import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


VECTOR_DB_PATH = "vectordb"


def get_vectorstore():
    # Load all .txt files from data folder
    documents = []
    for file in os.listdir("data"):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join("data", file), encoding="utf-8")
            docs = loader.load()
            for d in docs:
                d.metadata["source"] = file
            documents.extend(docs)

    if not documents:
        raise RuntimeError("No documents found in data folder")

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    split_docs = splitter.split_documents(documents)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create or load FAISS DB
    if os.path.exists(VECTOR_DB_PATH):
        vectorstore = FAISS.load_local(
            VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True
        )
    else:
        vectorstore = FAISS.from_documents(split_docs, embeddings)
        vectorstore.save_local(VECTOR_DB_PATH)

    return vectorstore
