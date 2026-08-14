import streamlit as st
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return text

def get_text_chunks(raw_text):
    text_splitter=characterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks= text_splitter.split_text(raw_text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings=HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore=FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore











def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs",page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    st.header("Chat with multiple PDFs :books:")
    user_question= st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs= st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True
                                   )
        if st.button("Process"):
            with st.spinner("Processing"):
                st.write("Processing your documents...")
                raw_text= get_pdf_text(pdf_docs)
                text_chunks= get_text_chunks(raw_text)
                st.success("Processing complete!")
                vectorstore=get_vectorstore(text_chunks)
                st.session_state.vectorstore=vectorstore
                st.success("Vectorstore created successfully!")



if __name_ == "__main__":
    main()           