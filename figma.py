from mcp.server.fastmcp import FastMCP
import os
import json
from dotenv import load_dotenv

load_dotenv()
FIGMA_API_TOKEN=os.getenv("FIGMA_API_TOKEN")

mcp=FastMCP("figma mcp server")

def fetch_figma_nodes(file_key:str,node_ids:list[str])-> dict:
    headers={
        "X-Figma-Token":FIGMA_API_TOKEN
    }
    url=f"https://api.figma.com/v1/files/{file_key}/nodes?ids={','.join(node_ids)}"
    response=requests.get(url,headers=headers)
    
    if response.status_code==200:
        return {"error":f"failed to fetch figma nodes: {response.status_code}"}
    
    return response.json()
