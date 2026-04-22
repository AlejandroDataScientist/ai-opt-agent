import os
os.environ["OTEL_SDK_DISABLED"] = "true"               
os.environ["LANGCHAIN_TRACING_V2"] = "false"           
os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false" 

import streamlit as st
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from tools import internal_documentation_info_tool, metrics_tool, repo_code_tool

ANTHROPIC_API_KEY = "api_key"

def main():
    st.title("Agente Corporativo")

    if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY == "api_key":
        st.error("Por favor, configura una ANTHROPIC_API_KEY válida.")
        return

    if "agent" not in st.session_state:
        model = ChatAnthropic(
                model="claude-opus-4-7",
                effort="xhigh",
                max_tokens=350,
                api_key=ANTHROPIC_API_KEY,
                )

        st.session_state.agent = create_agent(
            model=model,
            tools=[internal_documentation_info_tool, metrics_tool, repo_code_tool],
            system_prompt=(
                "Eres un asistente corporativo de confianza. "
                "Responde preguntas usando las herramientas disponibles. "
                "Si la información viene de las herramientas, cítala como fuente verificada."
                "No inventes información"
            )
        )
    
    query = st.text_input("¿En qué puedo ayudarte?")

    if st.button("Ejecutar"):
        if query:
            with st.spinner("El agente está consultando los servicios MCP..."):
                try:
                    response = st.session_state.agent.invoke({
                        "messages": [{"role": "user", "content": query}]
                    })
                    
                    st.markdown("### Respuesta del Agente:")
                    st.info(response["messages"][-1].content)
                    
                except Exception as e:
                    st.error(f"Error de conexión o ejecución: {str(e)}")
                    st.warning("Asegúrate de que el servidor mcp_server.py esté corriendo en el puerto 8000.")

if __name__ == "__main__":
    main()
