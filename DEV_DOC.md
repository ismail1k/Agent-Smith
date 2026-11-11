## Project Organization
Everything inside `src/` <br>
`src/console`: The **entry point** to the project, contain application commands. <br>
`src/resources/templates`: Contain templates that will be sent to the LLM.


## Available tools
| Tool | Description |
| :--- | :--- |
| template(name: str, **kwargs) | load template, first argument is the name of template (without .md), extra arguments are variables in the template defined using `{{ variable_name }}` |

Tools can be import from `src/utilities.py`, example:
```python
from src.utilities import tool_name
```


## OpenAI usage example
```python
from src.utilities import template
from src.services.LLMService import OpenAI

if __name__ == '__main__':
    llm = OpenAI()
    print(llm.chat([
        {
            'role': "system",
            'content': template('SYSTEM_PROMPT', agent_name="Smith")
        },
        {
            'role': "user",
            'content': "What's your name?"
        }
    ]))
```
- Available roles are: `system`, `user` and `assistant`.
- LLM must receive chat messages that has only one `system` completion.
- The LLM will reply with completion has role `assistant`


## About commands
First, create a python file located at `src/console/` with the following content:
```python
from src.utilities import Console


class group(Console):
    def command(self) -> None:
        pass
```
It will be discovered automatically, you can run the command using:
```bash
python -m src group command
```
or using uv:
```bash
uv run python -m src group command
```
