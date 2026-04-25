#from langchain_community.vectorstores import FAISS
#from langchain_google_genai import GoogleGenerativeAIEmbeddings

#def create_vectorstore(docs):
 #   embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#    return FAISS.from_documents(docs, embeddings)


from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    return FAISS.from_documents(docs, embeddings)