import PyPDF2
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def pdf_chat_interface():
    st.header("📄 PDF Intelligence")
    pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])

    if pdf_file:
        pdf_text = extract_text_from_pdf(pdf_file)
        st.text_area("PDF Preview", pdf_text[:1500], height=200)

        question = st.text_input("Ask a question about the PDF:")

        if question:
            # Split and embed
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            texts = text_splitter.split_text(pdf_text)
            embeddings = OpenAIEmbeddings()
            vectordb = Chroma.from_texts(texts, embedding=embeddings)

            docs = vectordb.similarity_search(question)
            llm = OpenAI(temperature=0)
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=question)

            st.success("Answer:")
            st.write(response)
