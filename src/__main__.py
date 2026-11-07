import importlib
import inspect
import pkgutil
import console
from fire import Fire


def load_cli_commands(package):
    commands = {}
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package.__name__}.{module_name}")
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) or inspect.isclass(obj):
                if obj.__module__ == module.__name__:
                    commands[name] = obj

    return commands

if __name__ == "__main__":
    Fire(load_cli_commands(console))
