import requests
from typing import Any


class OpenAI:
    base_url: str = "http://127.0.0.1:11434/v1"
    headers: dict = {"Accept": "application/json"}
    def __init__(self, model: str = 'qwen2.5-coder:3b') -> None:
        self.model: str = model

    def _endpoint(self, path: str) -> str:
        return f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"

    def chat(self, messages: list) -> dict | None:
        endpoint: str = self._endpoint('chat/completions')
        payload: dict = {'model': self.model, 'messages': messages}
        response = requests.post(endpoint, json=payload, headers=self.headers)
        return response.json()['choices'][0]['message']