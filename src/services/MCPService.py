from abc import ABC
from typing import Callable
from fastmcp import FastMCP
from fastmcp.prompts import prompt
from src.utilities.interfaces import Service


class MCPService(ABC):
    def __init__(self, server: FastMCP) -> None:
        self.__server


class MCPServer(Service, MCPService):
    def __init__(self, title: str = "MyMCP") -> None:
        MCPService.__init__(self, FastMCP(title))

    def http(self) -> None:
        self.__server.run(transport="http", host="0.0.0.0", port=9000)

    def stdio(self) -> None:
        self.__server.run()

    def add_tool(self, tool: Callable) -> None:
        self.__server.add_tool(tool)


class MCPClient(Service, MCPService):
    def __init__(self) -> None:
        MCPService.__init__(self, FastMCP(title))

    def discover(self) -> None:
        pass

    def call(self, tool: str) -> None:
        pass
