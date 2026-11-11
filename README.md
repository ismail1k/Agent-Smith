## Project Organization
Everything inside `src/` <br>
`src/console`: The **entry point** to the project, contain application command interfaces. <br>
Make a file inside and do a function/class, it will be discovered automatically. <br>
`src/resources/templates`: Contain prompt template that will be sent to the AI model
It can has dynamic variables


## Available tools
Tools can be import using:
```python
from src.utilities import tool_name
```

| Tool | Description |
| :--- | :--- |
| template(name: str, **kwargs) | load template, first argument is the name of template (without .md), extra arguments are variables in the template defined using `{{ variable_name }}` |


## OpenAI usage example
```python
from src.utilities import template
from src.plugins.LLMPlugin import OpenAI

if __name__ == '__main__':
    llm = OpenAI()
    print(llm.chat([
        {
            'role': "system",
            'content': template('SYSTEM_PROMPT', {'agent_name': 'Smith'})
        },
        {
            'role': "user",
            'content': "What's your name?"
        }
    ]))
```
Note: helpers (functions & classes) like `template` can be imported from `src.utilites`
