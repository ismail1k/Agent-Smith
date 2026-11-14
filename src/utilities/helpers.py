import re
from abc import ABC


def template(name: str, **kwargs) -> str:
    with open(f"src/resources/templates/{name}.md") as file:
        content: str = file.read()
        for key, value in kwargs.items():
            content = re.sub(
                r"\{\{\s*" + re.escape(key) + r"\s*\}\}",
                lambda _: str(value),
                content
            )
        return content


class TextManager:
    def __init__(self, string: str = "") -> None:
        self.__original: str = string
        self.__string: str = string

    @property
    def original(self) -> str:
        return self.__original

    @property
    def string(self) -> str:
        return self.__string

    def append(self, string: str = "") -> None:
        self.__original += string
        self.__string += string

    def extractPythonBlock(self) -> str | None:
        match = re.search(r"```python\s*\n(.*?)```", self.__string, re.DOTALL)
        if not match:
            return None
        code = match.group(1)
        self.__string = (
            self.__string[:match.start()] +
            self.__string[match.end():]
        )
        return code
