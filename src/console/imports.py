import builtins
import ast


ALLOWED_IMPORTS = [
    "math", "math.*",
    "collections", "collections.*",
    "itertools", "re", "json",
    "typing", "typing.*",
    "functools", "operator",
    "heapq", "bisect", "copy",
    "string", "random",
    "datetime", "datetime.*",
    "array", "cmath",
]

real_import = builtins.__import__

def is_allowed(name: str) -> bool:
    for rule in ALLOWED_IMPORTS:
        if rule.endswith(".*"):
            base = rule[:-2]
            if name.startswith(base):
                return True
        elif rule == name:
            return True
    return False


def safe_import(name: str, globals=None, locals=None, fromlist=(), level=0):
    if level != 0:
        raise ImportError("Relative imports are not allowed in the sandbox")
    if not is_allowed(name):
        raise ImportError(f"Import of '{name}' is not allowed in the sandbox")
    return real_import(name, globals, locals, fromlist, level)



def find_violations(code: str) -> list[str]:
    tree = ast.parse(code)
    problems = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr.startswith('_'):
                problems.append(
                    f"line {node.lineno}: access to '.{node.attr}' is not allowed "
                    f"(names starting with '_' are blocked)"
                )
        elif isinstance(node, ast.Name) and node.id.startswith('__'):
            problems.append(
                f"line {node.lineno}: use of '{node.id}' is not allowed"
            )
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.name.startswith('_'):
                    problems.append(
                        f"line {node.lineno}: importing '{alias.name}' is not allowed"
                    )
        
    return problems