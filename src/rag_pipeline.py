import os
import openai
import chromadb
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import streamlit as st

def rag_chat_interface():
    st.header("🧠 RAG Document Chat")
    uploaded_file = st.file_uploader("Upload a `.txt` file", type=["txt"])

    if uploaded_file:
        file_content = uploaded_file.read().decode("utf-8")
        st.text_area("Document Preview", file_content[:1000], height=200)

        question = st.text_input("Ask a question about this document:")

        if question:
            # Split and embed
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            texts = text_splitter.split_text(file_content)
            embeddings = OpenAIEmbeddings()
            vectordb = Chroma.from_texts(texts, embedding=embeddings)

            # Ask
            docs = vectordb.similarity_search(question)
            llm = OpenAI(temperature=0)
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=question)

            st.success("Answer:")
            st.write(response)
