from typing import Callable
from fastmcp import FastMCP
from fastmcp.prompts import prompt


class Server:
    def __init__(self, title: str = "MyMCP") -> None:
        self.server: FastMCP = FastMCP(title)

    def add_tool(self, tool: Callable) -> None:
        self.server.add_tool(tool)

    def http(self) -> None:
        self.server.run(transport="http", host="0.0.0.0", port=9000)

    def stdio(self) -> None:
        self.server.run()


class Client:
    def __init__(self) -> None:
        pass

    def discover(self) -> None:
        pass

    def call(self, tool: str) -> None:
        pass
