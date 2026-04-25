import streamlit as st

from loaders.pdf_loader import load_pdf
from loaders.docx_loader import load_docx
from processing.chunking import split_documents
from vectorstore.faiss_store import create_vectorstore
from rag.pipeline import create_rag_chain
import config  # loads API key

st.title("📄 AI Document Assistant (Gemini RAG)")

files = st.file_uploader(
    "Upload PDF or DOCX",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if files and st.button("Process"):
    docs = []

    for file in files:
        if file.name.endswith(".pdf"):
            docs.extend(load_pdf(file))
        elif file.name.endswith(".docx"):
            docs.extend(load_docx(file))

    chunks = split_documents(docs)
    vectorstore = create_vectorstore(chunks)

    st.session_state.qa_chain = create_rag_chain(vectorstore)
    st.success("Documents processed!")

query = st.text_input("Ask your question:")

if query and "qa_chain" in st.session_state:
    response = st.session_state.qa_chain.invoke(query)
    st.write("### Answer:")
    st.write(response.content)