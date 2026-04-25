from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file):
    with open("temp.pdf", "wb") as f:
        f.write(file.read())

    loader = PyPDFLoader("temp.pdf")
    return loader.load()