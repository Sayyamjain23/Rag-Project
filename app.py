import streamlit as st
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template



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

if __name_ == "__main__":
    main()           