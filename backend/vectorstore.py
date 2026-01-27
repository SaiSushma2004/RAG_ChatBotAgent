import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

VECTOR_DB_PATH = "vectordb"

def get_vectorstore():
    documents = []

    if not os.path.exists("data"):
        raise RuntimeError("data folder not found")

    for file in os.listdir("data"):
        if file.endswith(".txt"):
            loader = TextLoader(
                os.path.join("data", file),
                encoding="utf-8"
            )
            docs = loader.load()
            for d in docs:
                d.metadata["source"] = file
            documents.extend(docs)

    if not documents:
        raise RuntimeError("No documents found in data folder")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    split_docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",  # ✅ comma fixed
        model_kwargs={"device": "cpu"}
    )

    if os.path.exists(VECTOR_DB_PATH):
        vectorstore = FAISS.load_local(
            VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
    else:
        vectorstore = FAISS.from_documents(split_docs, embeddings)
        vectorstore.save_local(VECTOR_DB_PATH)

    return vectorstore
