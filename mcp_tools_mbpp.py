from fastmcp.tools import tool
from src.services.MCPService import Server


@tool()
def run_tests(code: str, test_list: list[str]) -> dict:
    return {}


if __name__ == "__main__":
    server = Server("MBPP Tools")
    server.add_tool(run_tests)
    server.http()
