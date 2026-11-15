import os
from src.utilities.interfaces import Console
from src.utilities.helpers import TextManager, template
from src.services import OpenAI, Sandbox


class AgentMBPP(Console):
    def handle(self) -> None:
        self.argparse.add_argument("--output", required=True)
        print(self.argparse.parse_args())
        print(os.getenv('PROVIDER_URL'))

        sandbox = Sandbox()
        canvas = TextManager()
        prompt: str = "Write a function to find the similar elements from the given two tuple lists.\nfunction_definition: def similar_elements(test_tup1, test_tup2):"
        llm = OpenAI(template('SYSTEM_PROMPT', agent_name="Smith"))
        for word in llm.chat(prompt):
            print(word, flush=True, end="")
            canvas.append(word)
            block = canvas.extractPythonBlock()
            if block:
                print('<output>', end="")
                sandbox.execute(block)
                print('</output>', end="")


if __name__ == '__main__':
    AgentMBPP("Agent MBPP")
