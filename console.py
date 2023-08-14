#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):

    """
    Class representing the command interpreter.
    """

    prompt = "(hbnb) "

    def __init__(self):
        """
        Initialize the command interpreter.
        """
        super().__init__()
        self._file_storage = FileStorage()

    def do_quit(self, args):
        """Quit command to exit the program."""
        print("Goodbye!")
        exit()

    def do_EOF(self, args):
        """Exit the program on EOF (Ctrl-D)"""
        print()  # Print a new line before exiting
        return True

    def do_help(self, args):
        """Help command to get help about commands."""
        if args:
            # If args is not empty, get help about a specific command
            try:
                command = getattr(self, "do_{}".format(args))
                print(command.__doc__)
            except AttributeError:
                print("Unknown command: {}".format(args))
        else:
            # If args is empty, print a list of all commands
            print("Documented commands (type help <topic>):")
            for command in self.get_commands():
                print("\t{}".format(command))

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def get_commands(self):
        """Get a list of all commands."""
        commands = []
        for command in dir(self):
            if command.startswith("do_"):
                commands.append(command[3:])
        return commands


if __name__ == "__main__":
    HBNBCommand().cmdloop()
