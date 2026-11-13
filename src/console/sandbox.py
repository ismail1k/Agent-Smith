import io
import contextlib
import traceback
import builtins
from src.console.imports import safe_import, find_violations


class Sandbox:
    def __init__(self) -> None:
        safe_builtins = dict(vars(builtins))
        safe_builtins['__import__'] = safe_import
        self.namespace: dict = {"__builtins__": safe_builtins}

    def run(self, code: str) -> str:
        """ """
        try:
            problems = find_violations(code)
        except SyntaxError as e:
            return f"syntax error on line {e.lineno}: {e.msg}"
        
        if problems:
            return f"code rejected by the sandbox:\n" + "\n".join(problems) + "\n"

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            try:
                exec(code, self.namespace)
            except Exception:
                return buffer.getvalue() + traceback.format_exc() 
        return buffer.getvalue()

def main():
    sandbox = Sandbox()
    while True:
        try:
            code = input(">>> ")
        except EOFError:
            print()
            break

        if code.strip() == "exit":
            break
        print(sandbox.run(code), end="")

# if __name__ == "__main__":
#     main()