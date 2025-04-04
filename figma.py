from mcp.server.fastmcp import FastMCP
import os
import json
from dotenv import load_dotenv
import requests
import sys
import argparse
from pathlib import Path


load_dotenv()
FIGMA_API_TOKEN=os.getenv("FIGMA_API_TOKEN")

mcp=FastMCP("figma mcp server")

def fetch_figma_nodes(file_key:str,node_ids:list[str])-> dict:
    headers={
        "X-Figma-Token":FIGMA_API_TOKEN
    }
    url=f"https://api.figma.com/v1/files/{file_key}/nodes?ids={node_ids}"
    response=requests.get(url,headers=headers)

    
    if response.status_code==200:
        return {"error":f"failed to fetch figma nodes: {response.status_code}"}
    
    return response.json()

@mcp.tool()
def get_node(file_key:str,node_id:str)->dict:
    """
    Get a node from a figma file
    Args:
        file_key{str}:the key of the figma file
        node_id{str}:the id of the node
    Returns:
        dict- the node data if found, empty dict if not found
    """
    if "-" in node_id and ":" not in node_id:
        node_id=node_id.replace("-",":")

    response=fetch_figma_nodes(file_key,[node_id])
    if "error" in response:
        return {"error":response["error"]}
    
    return response

def get_node_data(file_key:str,node_id:str)->dict:
    node=get_node(file_key,node_id)
    if "error" in node:
        return {"error":node["error"]}
    
    return node["data"]["nodes"][node_id]





file="war7ch3UIxia1m7y718uLU"
node="10:67"

print(get_node(file,node))

