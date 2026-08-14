# 📚 Chat with Multiple PDFs

A Streamlit web application that lets you upload multiple PDF documents and have a natural-language conversation with their content. Under the hood, it uses LangChain for orchestration, HuggingFace Instructor embeddings for semantic search, FAISS as the vector store, and Google's Gemini model for generating conversational answers.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-app-red)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

- 📄 Upload and process **multiple PDF files** at once
- ✂️ Automatic text extraction and chunking for efficient retrieval
- 🔍 Semantic search over document content using vector embeddings (FAISS)
- 💬 Conversational Q&A interface with **chat history/memory**
- 🤖 Powered by **Google Gemini** via `langchain-google-genai`
- 🎨 Custom chat UI with distinct user/bot message templates

---

## 🏗️ How It Works

1. **PDF Upload & Text Extraction** — PDFs are parsed page-by-page using `PyPDF2` and merged into a single raw text blob.
2. **Text Chunking** — The raw text is split into overlapping chunks using LangChain's `CharacterTextSplitter` to preserve context across boundaries.
3. **Embedding & Vector Store** — Each chunk is embedded using `HuggingFaceInstructEmbeddings` (`hkunlp/instructor-xl`) and stored in a local **FAISS** vector index.
4. **Conversational Retrieval Chain** — A `ConversationalRetrievalChain` combines the retriever with a Gemini LLM and a `ConversationBufferMemory` so follow-up questions retain context.
5. **Chat UI** — User and AI messages are rendered in Streamlit using custom HTML/CSS templates.

---

## 🛠️ Tech Stack

| Component | Library / Service |
|---|---|
| Web UI | [Streamlit](https://streamlit.io/) |
| PDF Parsing | [PyPDF2](https://pypi.org/project/PyPDF2/) |
| Orchestration | [LangChain](https://www.langchain.com/) |
| Embeddings | HuggingFace Instructor (`hkunlp/instructor-xl`) |
| Vector Store | [FAISS](https://github.com/facebookresearch/faiss) |
| LLM | Google Gemini (`langchain-google-genai`) |
| Env Management | [python-dotenv](https://pypi.org/project/python-dotenv/) |

---

## 📋 Prerequisites

- Python 3.9 or higher
- A **Google API key** with access to the Gemini API ([Google AI Studio](https://aistudio.google.com/))
- pip / virtualenv (recommended)

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > If you don't have a `requirements.txt` yet, create one with at least:
   > ```
   > streamlit
   > python-dotenv
   > PyPDF2
   > langchain
   > langchain-community
   > langchain-google-genai
   > InstructorEmbedding
   > sentence-transformers
   > faiss-cpu
   > ```

4. **Set up environment variables**

   Create a `.env` file in the project root:

   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

---

## ▶️ Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   (Replace `app.py` with the actual filename of the script.)

2. Open the app in your browser (Streamlit will provide a local URL, typically `http://localhost:8501`).

3. In the sidebar:
   - Upload one or more PDF files
   - Click **"Process"** to extract text, generate embeddings, and build the vector store

4. In the main panel:
   - Type a question about your uploaded documents into the text input
   - Press Enter to receive an answer grounded in the PDF content
   - Continue the conversation — chat history is preserved for context-aware follow-ups

---

## 📁 Project Structure

```
.
├── app.py                 # Main Streamlit application
├── htmlTemplates.py        # CSS and HTML templates for chat bubbles
├── requirements.txt        # Python dependencies
├── .env                     # Environment variables (not committed)
└── README.md                # Project documentation
```

---

## ⚠️ Notes & Known Considerations

- **Model name**: the code references `gemini-3.6-flash` — verify this against the [currently available Gemini model names](https://ai.google.dev/gemini-api/docs/models) before running, as model identifiers change over time and an invalid name will cause API errors.
- **Instructor embeddings** (`hkunlp/instructor-xl`) are large and will download several GB of model weights on first run; ensure you have sufficient disk space and RAM, or swap in a lighter embedding model if needed.
- The vector store is currently held **in-memory** per session (via `st.session_state`) and is not persisted to disk — re-processing is required after restarting the app.
- No `requirements.txt` was included with the shared script; make sure to generate/pin one (`pip freeze > requirements.txt`) for reproducible installs.

---

## 🗺️ Roadmap Ideas

- [ ] Persist FAISS index to disk to avoid reprocessing on every session
- [ ] Add support for other document types (DOCX, TXT, web URLs)
- [ ] Add source citation/highlighting for retrieved answer snippets
- [ ] Dockerize the application for easier deployment
- [ ] Add unit tests for text extraction and chunking logic

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it.

---

## 🙏 Acknowledgements

- [LangChain](https://www.langchain.com/) for the orchestration framework
- [HuggingFace](https://huggingface.co/) for the Instructor embedding models
- [Facebook Research FAISS](https://github.com/facebookresearch/faiss) for efficient vector search
- [Streamlit](https://streamlit.io/) for the rapid UI framework
- [Google Gemini](https://ai.google.dev/) for the conversational LLM
