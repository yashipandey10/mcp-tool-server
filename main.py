from fastapi import FastAPI
from pydantic import BaseModel
from tools_registry import TOOLS
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
def format_response(status: str,message: str,tool: str=None,result=None):
    return{
        "status":status,
        "tool":tool,
        "message":message,
        "result":result
    }
app=FastAPI()
logging.info("MCP Server Started")
class MCPRequest(BaseModel):
    tool:str
    data:dict
@app.get("/")
def home():
    return {"message": "Hello! Your first server is running"}
@app.post("/mcp")
def mcp_handler(request: MCPRequest):
    logging.info(f"Incoming request for tool: {request.tool}")
    tool_name =request.tool
    if tool_name not in TOOLS:
       return format_response("error",f"Tool '{tool_name}' not found")
    tool_info=TOOLS[tool_name]
    func=tool_info["function"]
    expected_fields=tool_info["expected_feilds"]

    for field in expected_fields:
        if field not in request.data:
            logging.error(f"Missing field '{field}' for tool '{tool_name}'")
            return format_response("error", f"Missing field: {field}", tool_name)
    try:
       result = func(*request.data.values())
       return format_response("success", "Tool execution successful", tool_name, result)
    
    except Exception as e :
       logging.exception(f"Error executing tool '{tool_name}'")
       return format_response("error ",f"server crashed : {str(e)} ",request.tool) 
