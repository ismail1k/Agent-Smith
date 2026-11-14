from abc import ABC
from src.utilities.interfaces import Service


class SBService(ABC):
    pass


class Sandbox(Service, SBService):
    def __init__(self) -> None:
        pass

    def execute(self, code: str) -> str:
        return exec(code)
