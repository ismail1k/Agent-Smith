import sys
from abc import ABC
from dotenv import load_dotenv
from argparse import ArgumentParser
from src.utilities.exceptions import ConsoleException


class Console(ABC):
    def __init__(self, description: str):
        try:
            load_dotenv()
            self.argparse = ArgumentParser(description=description)
            try:
                self.handle()
            except KeyboardInterrupt:
                raise ConsoleException('KeyboardInterrupt')
                sys.exit(1)
            except FileNotFoundError:
                raise ConsoleException('FileNotFoundError')
                sys.exit(1)
            except PermissionError:
                raise ConsoleException('PermissionError')
                sys.exit(1)
        except ConsoleException as exception:
            print(exception)
            sys.exit(1)


class Service(ABC):
    def __init__(self):
        pass
