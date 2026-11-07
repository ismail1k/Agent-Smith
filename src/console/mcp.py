from vendor import Console
from plugins.MCPPlugin import Server as MCPServer


class MCPServe(Console):
    """Run MCP Server"""
    def __init__(self) -> None:
        server: MCPServer = MCPServer()
        server.http()
