from src.utilities import Console
from src.services.MCPService import Server as MCPServer


class mcp(Console):
    def __init__(self) -> None:
        self.server: MCPServer = MCPServer()

    def stdio(self) -> None:
        """Serve using stdio"""
        self.server.stdio()

    def http(self) -> None:
        """Serve using http"""
        self.server.http()
