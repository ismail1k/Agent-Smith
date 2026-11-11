import re
from abc import ABC
from typing import Any


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


class Console(ABC):
    pass
