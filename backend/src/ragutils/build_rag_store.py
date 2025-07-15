"""
Run once to embed every file in ./data and save a FAISS index in ./rag_store
"""

from pathlib import Path
from dotenv import load_dotenv

from langchain.document_loaders import (
    DirectoryLoader,
    TextLoader,
    UnstructuredPDFLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


load_dotenv()                       # picks up GEMINI_API_KEY
EMBED_MODEL = "models/embedding-001"
STORE_PATH  = "rag_store"

### 1) Load every file -------------------------------------------------
docs = []
docs += DirectoryLoader("ragutils/data", glob="**/*.txt", loader_cls=TextLoader).load()
docs += DirectoryLoader("ragutils/data", glob="**/*.md",  loader_cls=TextLoader).load()
docs += DirectoryLoader("ragutils/data", glob="**/*.pdf", loader_cls=UnstructuredPDFLoader).load()


### 2) Split into ~500‑token chunks -----------------------------------
splitter  = RecursiveCharacterTextSplitter(
    chunk_size=2000,  # chars ≈ 500 tokens
    chunk_overlap=200,
)
chunks = splitter.split_documents(docs)

### 3) Embed + write FAISS --------------------------------------------
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local(STORE_PATH)

print(f"  Stored {len(chunks):,} chunks in {STORE_PATH}/")
