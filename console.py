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

    # New commands

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.

        Args:
            args: The class name of the new instance.

        Example:
            $ create BaseModel
        """
        if not args:
            print("** class name missing **")
            return

        class_name = args
        try:
            b = BaseModel(class_name)
            self._file_storage.save()
            print(b.id)
        except ValueError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id.

        Args:
            args: The class name and id of the instance to print.

        Example:
            $ show BaseModel 1234-1234-1234
        """
        if not args:
            print("** instance id missing **")
            return

        class_name, id = args.split(" ")
        try:
            b = self._file_storage.get(class_name, id)
            if b is None:
                print("** no instance found **")
            else:
                print(b)
        except ValueError:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file).

        Args:
            args: The class name and id of the instance to delete.

        Example:
            $ destroy BaseModel 1234-1234-1234
        """
        if not args:
            print("** class name missing **")
            return

        class_name, id = args.split(" ")
        try:
            b = self._file_storage.get(class_name, id)
            if b is None:
                print("** no instance found **")
            else:
                del self._file_storage._objects[class_name + "." + id]
                self._file_storage.save()
        except ValueError:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name.

        Args:
            args: The class name (optional).
