import os    
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

RAW = Path('data/raw/politicas.md')
DB_PATH = 'data/data_db'

def vectorstore():
    if not RAW.exists():
        raise FileNotFoundError(f"No se encontró: {RAW}")
    
    loader = TextLoader(str(RAW), encoding='utf-8')
    documents = loader.load()
    
    split = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50
    )
    
    chunks = split.split_documents(documents)
    
    embeddings = OllamaEmbeddings(
        model = "nomic-embed-text", 
        base_url = "http://localhost:11434"
    )
    
    db = Chroma.from_documents(
        documents = chunks,
        embedding = embeddings,
        persist_directory = DB_PATH
    )
    
    print(f"Base de datos creada en: {DB_PATH}")

def main():
    vectorstore()
    print('Done')
    
if __name__ == '__main__':
    main()
