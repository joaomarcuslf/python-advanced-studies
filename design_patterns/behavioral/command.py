from abc import ABC, abstractmethod


class Invoker:
    def __init__(self):
        self._commands = {}
        self._history = []

    @property
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name, *args):
        if command_name in self._commands.keys():
            self._history.append(command_name)

            self._commands[command_name].execute(*args)
        else:
            print(f"Command [{command_name}] not recognised")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LikeCommand(Command):
    def execute(self, *args):
        print(f"{args[0]} liked {args[1]}.")


class TagCommand(Command):
    def execute(self, *args):
        print(f"{args[0]} tagged {args[1]}.")


""" USAGE:
invoker = Invoker()
invoker.register("LIKE", LikeCommand())
invoker.register("TAG", TagCommand())

invoker.execute("LIKE", "João", "Letícia")
invoker.execute("TAG", "João", "Letícia")

print(invoker.history)
"""
