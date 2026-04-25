

# 📄 AI Document Assistant (Gemini RAG)
<img width="1920" height="1080" alt="Screenshot (10)" src="https://github.com/user-attachments/assets/6139ef23-2c9e-4678-af1c-820d7534a7b4" />


## 🚀 Overview
AI Document Assistant is a Retrieval-Augmented Generation (RAG) based application that allows users to upload PDF/DOCX files and ask questions about their content. The system retrieves relevant information from the documents and generates accurate, context-aware responses using Google Gemini LLM.

---

## ✨ Features
- 📂 Upload PDF and DOCX files  
- 🔍 Intelligent document chunking and retrieval  
- 🧠 Semantic search using embeddings + FAISS  
- 🤖 Context-aware answers using Gemini LLM  
- ⚡ Real-time query interface with Streamlit  
- 🧩 Modular architecture (loaders, processing, vectorstore, pipeline)

---

## 🏗️ Architecture
```

Document Upload → Text Extraction → Chunking → Embeddings → FAISS Vector DB
→ Retrieval → Gemini LLM → Answer Generation

```

---

## 🛠️ Tech Stack
- Python  
- LangChain  
- Google Gemini API  
- FAISS (Vector Database)  
- HuggingFace Embeddings  
- Streamlit  
- PyPDF / python-docx  

---

## 📁 Project Structure
```

ai-project/
│
├── app.py                  # Streamlit app
├── config.py               # API key setup
│
├── loaders/
│   ├── pdf_loader.py
│   └── docx_loader.py
│
├── processing/
│   └── chunking.py
│
├── vectorstore/
│   └── faiss_store.py
│
├── rag/
│   └── pipeline.py
│
└── requirements.txt

````

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ai-document-assistant.git
cd ai-document-assistant

python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
````

---

## 🔑 Setup API Key

Create a `.env` file or use config:

```python
import os
os.environ["GOOGLE_API_KEY"] = "your_api_key_here"
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 💡 How It Works

1. Upload document (PDF/DOCX)
2. Text is extracted and split into chunks
3. Chunks are converted into embeddings
4. Stored in FAISS vector database
5. User asks a question
6. Relevant chunks are retrieved
7. Gemini LLM generates final answer

---

## 📌 Example Use Cases

* Ask questions from job descriptions
* Summarize documents
* Extract key insights
* Analyze reports

---

## 🚧 Future Improvements

* Chat history support
* Multi-document comparison
* Deployment (Streamlit Cloud / AWS)
* Agent-based workflows

---

## 👨‍💻 Author

Ayesha

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

````

---

# 🎯 What to do next

👉 Replace:
- `your-username`  
- `Your Name`  

👉 (Optional but HIGHLY recommended)
Add screenshot like:

```markdown
## 📸 Demo

![App Screenshot](your-image-path.png)
````

---

If you want, I can:
👉 optimize this README to look **top-tier (badges + demo + recruiter friendly)**
