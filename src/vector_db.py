from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS, Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

def build_vector_store_from_file(file_path, use_chroma=False, persist_dir="vector_db"):
    """Builds a vector store (FAISS or Chroma) from a given text file."""
    loader = TextLoader(file_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    if use_chroma:
        db = Chroma.from_documents(docs, embeddings, persist_directory=persist_dir)
        db.persist()
    else:
        db = FAISS.from_documents(docs, embeddings)

    return db

def load_vector_store(persist_dir="vector_db", use_chroma=False):
    """Loads the vector store from disk."""
    embeddings = OpenAIEmbeddings()
    if use_chroma:
        return Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    else:
        raise NotImplementedError("Only Chroma persistence supported currently.")
