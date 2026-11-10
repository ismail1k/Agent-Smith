import re
from abc import ABC
from typing import Any


class Console(ABC):
    pass


class Prompts:
    @prompt()
    @staticmethod
    def system_prompt(variables: dict[str, Any]) -> str:
        with open('src/resources/templates/SYSTEM_PROMPT.md') as file:
            content: str = file.read()
            for key in variables.keys():
                content = re.sub(
                    r"\{\{\s*" + re.escape(key) + r"\s*\}\}",
                    lambda _: str(variables[key]),
                    content
                )
            return content
