class ConsoleException(Exception):
    def __init__(self, message: str):
        super().__init__(f"\n\033[31mConsoleException:\033[0m {message}")


class ServiceException(Exception):
    def __init__(self, message: str):
        super().__init__(f"\033[31mServiceException:\033[0m {message}")
