from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

DB_PATH = "data/data_db_scripts"

def repo_code_tool(query: str) -> str:
    """
    Analiza el código fuente del repositorio. 
    Úsala para entender cómo funcionan las fórmulas y la lógica del software.
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
