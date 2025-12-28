from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import os

DATA_PATH = "../data"
DB_PATH = "../vectordb"

documents = []

for file in os.listdir(DATA_PATH):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(DATA_PATH, file))
        documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L3-v2"
)

db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory=DB_PATH
)

db.persist()
print("✅ Documents ingested successfully")
