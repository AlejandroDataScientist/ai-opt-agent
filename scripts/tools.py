import requests
from langchain.tools import tool

BASE_URL = "http://127.0.0.1:8000"

@tool
def metrics_tool(query: str) -> str:
    """
    Proporciona las métricas del sistema en tiempo real (CPU, memoria, disco).
    Úsala para diagnosticar lentitud o estado del hardware.
    """
    response = requests.post(f"{BASE_URL}/tools/metrics", json={"query": query})
    return response.json()["output"]

@tool
def internal_documentation_info_tool(query: str) -> str:
    """
    Consulta la base de datos de políticas de la empresa (RAG). 
    Úsala para dudas sobre normativas, vestimenta, horarios y beneficios.
    """
    response = requests.post(f"{BASE_URL}/tools/policies", json={"query": query})
    return response.json()["output"]

@tool
def repo_code_tool(query: str) -> str:
    """
    Analiza el código fuente del repositorio. 
    Úsala para entender cómo funcionan las fórmulas y la lógica del software.
    """
    response = requests.post(f"{BASE_URL}/tools/repo", json={"query": query})
    return response.json()["output"]
