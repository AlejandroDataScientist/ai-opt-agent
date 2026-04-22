from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

DB_PATH = "data/data_db"

def internal_documentation_info_tool(query: str) -> str:
    """Consulta la base de datos de políticas de la empresa (RAG). 
       Úsala para dudas sobre normativas, vestimenta, horarios y beneficios.
    """
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text", 
        base_url="http://localhost:11434"
    )
    
    db = Chroma(
        persist_directory=DB_PATH, 
        embedding_function=embeddings
    )
    
    docs = db.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in docs])
