# rag_retriever.py – centralized retriever for FAISS‑based RAG
from __future__ import annotations
import os, pathlib
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

# 1) Load environment file located in the repo root (one level up from backend/)
load_dotenv()   

# 2) Vector‑store folder sits in backend/rag_store
default_store = pathlib.Path(__file__).resolve().parents[1] / "rag_store"
STORE_PATH = pathlib.Path(os.getenv("RAG_VECTORSTORE_PATH", default_store))

# Config overrides (optional)
EMBED_MODEL = os.getenv("RAG_EMBED_MODEL")
TOP_K       = int(os.getenv("RAG_TOP_K", 6))

# Embeddings
embeddings = OpenAIEmbeddings(model=EMBED_MODEL) if EMBED_MODEL else OpenAIEmbeddings()

# Fail fast if store missing
if not STORE_PATH.exists():
    raise RuntimeError(
        f"Vector store not found at '{STORE_PATH}'.\n"
        "→ Run backend/ragutils/build_rag_store.py first."
    )

# Load FAISS index and expose retriever
vectorstore = FAISS.load_local(
    str(STORE_PATH),
    embeddings,
    allow_dangerous_deserialization=True
)
retriever   = vectorstore.as_retriever(search_kwargs={"k": TOP_K})
