## Utilities
Tools can be import from `src/utilities.py`, example:
```python
from src.utilities import tool_name
```

| Function | Description |
| :--- | :--- |
| template(name: str, **kwargs) | load template, first argument is the name of template (without .md), extra arguments are variables in the template defined using `{{ variable_name }}` |

TextManager to manipulate text/string:
```python
string = "Lorem ipsum dolor sit amet: ```python print('python code') ```"
canvas = TextManager(string)
```
You can extract the python block by using `extractPythonBlock()` method
```python
print(canvas.extractPythonBlock())
# output: "print('python code')"
```
`extractPythonBlock` method remove the extracted part from the original string.
```python
print(canvas.string)
# output: "Lorem ipsum dolor sit amet: "
```
If you want to get all string incuding extracted parts, you use property `original`
```python
print(canvas.original)
# output: "Lorem ipsum dolor sit amet: ```python print('python code') ```"
```


## OpenAI usage example
```python
from src.utilities import template
from src.services.LLMService import OpenAI

if __name__ == '__main__':
    llm = OpenAI()
    messages: list = [
        {
            'role': "system",
            'content': template('SYSTEM_PROMPT', agent_name="Smith")
        },
        {
            'role': "user",
            'content': "What's your name?"
        }
    ]
    for word in llm.chat(messages):
        print(word, end="", flush=True)
```
- Available roles are: `system`, `user` and `assistant`.
- LLM must receive chat messages that has only one `system` completion.
- The LLM will reply with completion has role `assistant`

`llm.chat()` by default stream the response, if you want to turn off the stream mode, you can set it as an argument:
```python
llm.chat(messages, stream=False)
```
