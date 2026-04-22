from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from tool_metricas_sistema import metrics_tool
from tool_politicas import internal_documentation_info_tool
from tool_repo import repo_code_tool

app = FastAPI(
    title="MCP Server",
)

class ToolRequest(BaseModel):
    query: str
    
@app.post("/tools/metrics")
async def get_metrics(request: ToolRequest):
    try:
        result = metrics_tool(request.query)
        return {"output": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tools/policies")
async def get_policies(request: ToolRequest):
    try:
        result = internal_documentation_info_tool(request.query)
        return {"output": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tools/repo")
async def get_repo_info(request: ToolRequest):
    try:
        result = repo_code_tool(request.query)
        return {"output": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
