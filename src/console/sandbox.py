import io
import contextlib
import traceback

class Sandbox:
    def __init__(self) -> None:
        self.namespace: dict = {} 

    def run(self, code: str) -> str:
        """ """
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