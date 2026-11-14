import json
import requests
from abc import ABC, abstractmethod
from src.utilities.interfaces import Service


class LLMService(ABC):
    def __init__(self, base_url: str, model: str) -> None:
        self.model: str = model
        self.base_url: str = base_url
        self.headers: dict = {"Accept": "application/json"}

    def _endpoint(self, path: str) -> str:
        return f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"

    @abstractmethod
    def chat(self, messages: list, stream: bool = True) -> dict:
        pass


class LLMUsageTracker(ABC):
    def __init__(self) -> None:
        self.__usage: dict = {}

    def track(self, usage: dict) -> None:
        self.__usage: dict = usage

    def usage(self) -> dict:
        return self.__usage


class OpenAI(Service, LLMService, LLMUsageTracker):
    def __init__(self, base_url: str = 'http://127.0.0.1:11434/v1', model: str = 'qwen2.5-coder:3b') -> None:
        LLMService.__init__(self, base_url, model)
        LLMUsageTracker.__init__(self)

    def chat(self, messages: list, stream: bool = True) -> dict:
        endpoint: str = self._endpoint('chat/completions')
        payload: dict = {'model': self.model, 'messages': messages, 'stream': stream}
        response = requests.post(endpoint, json=payload, headers=self.headers, stream=stream)
        for line in response.iter_lines():
            if line:
                line = line.decode("utf-8")
                if line.startswith("data: "):
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    chunk = json.loads(data)
                    yield chunk["choices"][0]["delta"].get("content", "")
        return {}
