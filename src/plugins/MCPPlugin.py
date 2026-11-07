from fastmcp import FastMCP
from fastmcp.tools import tool


class Tools:
    @tool()
    @staticmethod
    def tool_one(self) -> None:
        print("tool_one executed")


class Server:
    def __init__(self) -> None:
        self.server: FastMCP = FastMCP("MyMCP")
        self.server.add_tool(Tools.tool_one)

    def stdio(self) -> None:
        return self.server.run()

    def http(self) -> None:
        return self.server.run(transport="http", host="0.0.0.0", port=9000)
