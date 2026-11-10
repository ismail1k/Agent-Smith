from fastmcp.tools import tool
from src.plugins.MCPPlugin import Server


@tool()
def read_file() -> None:
    return None

@tool()
def edit_file() -> None:
    return None

@tool()
def list_files() -> None:
    return None

@tool()
def search_code() -> None:
    return None

@tool()
def search_function_or_class_definition_in_code() -> None:
    return None

@tool()
def find_references() -> None:
    return None

@tool()
def run_tests() -> None:
    return None

@tool()
def get_patch() -> None:
    return None

@tool()
def run_command() -> None:
    return None


if __name__ == "__main__":
    server = Server("SWE-bench Tools")
    server.add_tool(read_file)
    server.add_tool(edit_file)
    server.add_tool(list_files)
    server.add_tool(search_code)
    server.add_tool(search_function_or_class_definition_in_code)
    server.add_tool(find_references)
    server.add_tool(run_tests)
    server.add_tool(get_patch)
    server.add_tool(run_command)
    server.http()
