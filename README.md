## Resumen del Proyecto

Este sistema es un Agente Corporativo Inteligente diseñado para centralizar la consulta de normativas internas, el análisis de código fuente y el monitoreo del estado del sistema en tiempo real. Utiliza una arquitectura de Generación Aumentada por Recuperación (RAG) y se integra mediante el estándar Model Context Protocol (MCP) para exponer herramientas especializadas a un modelo de lenguaje de gran escala (Claude 3 Opus).

---

## Arquitectura Técnica

El proyecto se divide en cuatro capas principales:

1. **Capa de Ingesta y Validación**: Los scripts de ingesta procesan documentos Markdown y archivos Python, generando un manifiesto con hashes SHA-256 para garantizar la integridad de los datos en la transición de la etapa de origen (source) a la etapa de procesamiento (raw).
2. **Capa de Persistencia Vectorial**: Utiliza ChromaDB y modelos de embedding locales (nomic-embed-text vía Ollama) para indexar la documentación y el código fuente, permitiendo búsquedas semánticas eficientes mediante segmentación de texto especializada.
3. **Capa de Servicio (MCP Server)**: Un servidor basado en FastAPI que actúa como puente, exponiendo las capacidades de consulta de base de datos y métricas de sistema a través de endpoints estandarizados accesibles para el agente.
4. **Capa de Interfaz (Streamlit)**: Una aplicación web que orquesta la interacción entre el usuario y el agente de IA, gestionando el flujo de trabajo y la invocación de herramientas.

---

## Estructura del Directorio

* **data/**: Almacena las bases de datos vectoriales persistentes y los archivos en sus estados raw y source.
* **notebooks/**: Espacio para experimentación, pruebas de recuperación de datos y prototipado.
* **scripts/**: Núcleo lógico del sistema:
    * `ingest_*.py`: Automatización de la carga y validación de archivos fuente.
    * `*_vectorstores.py`: Creación y persistencia de los índices en ChromaDB.
    * `mcp_server.py`: Servidor de herramientas basado en FastAPI.
    * `streamlit_app.py`: Aplicación cliente principal.
    * `tools.py` / `tool_*.py`: Definición de la lógica de herramientas para métricas, políticas y repositorio.

---

## Requisitos del Sistema

* Python 3.10 o superior.
* Ollama instalado y ejecutando el modelo `nomic-embed-text`.
* Dependencias principales: `streamlit`, `langchain`, `fastapi`, `uvicorn`, `chromadb`, `psutil`, `requests`, `langchain-anthropic`.

---

## Procedimiento de Configuración

1. **Ingesta de Datos**:
   Ejecutar los comandos para validar y trasladar los archivos fuente:
   `python scripts/ingest_politica_interna.py`
   `python scripts/ingest_repositories.py`

2. **Indexación Vectorial**:
   Generar los almacenes de vectores para las búsquedas RAG:
   `python scripts/piliticas_vectorstore.py`
   `python scripts/repositories_vectorstores.py`

3. **Ejecución del Servidor MCP**:
   Iniciar el backend que sirve las herramientas al agente:
   `python scripts/mcp_server.py`

4. **Lanzamiento de la Interfaz**:
   Iniciar la aplicación de usuario final:
   `streamlit run scripts/streamlit_app.py`

---

# English Version

## Project Overview

This system is a Corporate Intelligent Agent designed to centralize the consultation of internal regulations, source code analysis, and real-time system status monitoring. It utilizes a Retrieval-Augmented Generation (RAG) architecture and integrates via the Model Context Protocol (MCP) standard to expose specialized tools to a Large Language Model (Claude 3 Opus).

---

## Technical Architecture

The project is structured into four primary layers:

1. **Ingestion and Validation Layer**: Ingestion scripts process Markdown documents and Python files, generating a manifest with SHA-256 hashes to ensure data integrity during the transition from source to raw processing stages.
2. **Vector Persistence Layer**: Employs ChromaDB and local embedding models (nomic-embed-text via Ollama) to index documentation and source code, enabling efficient semantic searches through specialized text splitting.
3. **Service Layer (MCP Server)**: A FastAPI-based server acting as a bridge, exposing database query capabilities and system metrics through standardized endpoints accessible to the agent.
4. **Interface Layer (Streamlit)**: A web application that orchestrates the interaction between the user and the AI agent, managing the workflow and tool invocation.

---

## Directory Structure

* **data/**: Stores persistent vector databases and files in raw/source states.
* **notebooks/**: Experimental space for data retrieval testing and prototyping.
* **scripts/**: Logic core of the system:
    * `ingest_*.py`: Automation of source file loading and validation.
    * `*_vectorstores.py`: Creation and persistence of ChromaDB indices.
    * `mcp_server.py`: FastAPI-based tool server.
    * `streamlit_app.py`: Main client application.
    * `tools.py` / `tool_*.py`: Logical definition of tools for metrics, policies, and repository analysis.

---

## System Requirements

* Python 3.10 or higher.
* Ollama installed and running the `nomic-embed-text` model.
* Key dependencies: `streamlit`, `langchain`, `fastapi`, `uvicorn`, `chromadb`, `psutil`, `requests`, `langchain-anthropic`.

---

## Setup Procedure

1. **Data Ingestion**:
   Run the commands to validate and transfer source files:
   `python scripts/ingest_politica_interna.py`
   `python scripts/ingest_repositories.py`

2. **Vector Indexing**:
   Generate the vector stores for RAG searches:
   `python scripts/piliticas_vectorstore.py`
   `python scripts/repositories_vectorstores.py`

3. **MCP Server Execution**:
   Start the backend serving the tools to the agent:
   `python scripts/mcp_server.py`

4. **Interface Launch**:
   Start the final user application:
   `streamlit run scripts/streamlit_app.py`
