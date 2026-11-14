import json
import requests
from abc import ABC, abstractmethod
from src.utilities.interfaces import Service


class LLMService(ABC):
    def __init__(self, base_url: str, model: str) -> None:
        self.model: str = model
        self.base_url: str = base_url

    def _endpoint(self, path: str) -> str:
        return f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"

    @abstractmethod
    def chat(self, messages: list, stream: bool = True) -> dict:
        pass


class LLMMetrics(ABC):
    def __init__(self) -> None:
        self.__usage: int = 0

    @property
    def usage(self) -> int:
        return self.__usage

    @usage.setter
    def usage(self, tokens: int) -> None:
        self.__usage += tokens


class OpenAI(Service, LLMService, LLMMetrics):
    def __init__(self, system_prompt: str) -> None:
        LLMService.__init__(self, 'http://127.0.0.1:11434/v1', 'qwen2.5-coder:3b')
        LLMMetrics.__init__(self)
        self.messages: list = []
        self.messages.append({'role': "system", 'content': system_prompt})

    def chat(self, prompt: str, tools: list = [], stream: bool = True) -> dict:
        self.messages.append({'role': "user", 'content': prompt})
        response = requests.post(
            self._endpoint('chat/completions'),
            stream=stream, json={
                'model': self.model,
                'messages': self.messages,
                'stream': stream,
                'stream_options': {
                    'include_usage': True
                }
            },
        )
        if stream == False:
            return response.json()
        chunks: list = []
        for chunk in response.iter_lines():
            chunk = chunk.decode("utf-8")
            if chunk.startswith("data: "):
                if '[DONE]' in chunk:
                    break
                content = json.loads(chunk[6:])
                chunks.append(content)
                if len(content['choices']):
                    yield content['choices'][0]['delta']['content']
                if 'usage' in content:
                    self.usage = content['usage']['total_tokens']
