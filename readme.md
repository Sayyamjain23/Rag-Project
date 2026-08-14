# Multi-PDF Chat Assistant

A Retrieval-Augmented Generation (RAG) application built with Streamlit and LangChain. This application allows users to upload multiple PDF documents, process them into a local vector database, and interactively ask questions about the content using Google's Gemini AI model. The assistant maintains conversational memory, allowing for context-aware follow-up questions.

---

## 🚀 Features

* **Multi-Document Processing:** Upload and parse multiple PDF files simultaneously.
* **Semantic Search:** Utilizes high-quality HuggingFace Instruct embeddings for accurate text retrieval.
* **Conversational Memory:** Remembers the context of the current chat session for natural, flowing conversations.
* **Google Gemini Integration:** Powered by the fast and capable `gemini-3.6-flash` model via the Google Generative AI API.
* **Interactive UI:** Clean, user-friendly web interface built with Streamlit, featuring custom message templates.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **LLM Orchestration:** LangChain
* **Generative AI:** Google Gemini API (`gemini-3.6-flash`)
* **Embeddings:** HuggingFace (`hkunlp/instructor-xl`)
* **Vector Database:** FAISS (Facebook AI Similarity Search)
* **Document Parsing:** PyPDF2

---

## 📋 Prerequisites

Before running the application, ensure you have Python installed (3.8 or higher recommended). You will also need a free API key from Google AI Studio.

1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Ensure you have the necessary build tools installed for FAISS and related local embedding libraries.

---

## ⚙️ Installation & Setup

Follow these exact steps to install and set up the project on your local machine:

**1. Clone the repository**
```bash
git clone [https://github.com/Sayyamjain23/Rag-Project.git](https://github.com/Sayyamjain23/Rag-Project.git)
cd Rag-Project