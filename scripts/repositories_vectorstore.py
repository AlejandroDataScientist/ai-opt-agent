import os
from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

SOURCE_DIR = Path('data/raw') 
DB_PATH = 'data/data_db_scripts'

def vectorstore():
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(f"No se encontró la carpeta: {SOURCE_DIR}")
    
    loader = DirectoryLoader(
        str(SOURCE_DIR), 
        glob="**/*.py", 
        loader_cls=TextLoader, 
        loader_kwargs={'encoding': 'utf-8'}
    )
    documents = loader.load()
    
    split = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=1000,
        chunk_overlap=150
    )
    
    chunks = split.split_documents(documents)
    
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text", 
        base_url="http://localhost:11434"
    )
    
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )
    
    print(f"Base de datos de scripts creada en: {DB_PATH}")
    print(f"Documentos procesados: {len(documents)}")
    print(f"Fragmentos generados: {len(chunks)}")

def main():
    vectorstore()
    print('Done')
    
if __name__ == '__main__':
    main()
