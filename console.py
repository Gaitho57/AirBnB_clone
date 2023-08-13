import cmd
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Goodbye!")
        exit()

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)"""
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_help(self, args):
        """Help command to get help about commands"""
        if args:
            if args in self.commands:
                print(self.commands[args].__doc__)
            else:
                print("Unknown command: {}".format(args))
        else:
            print("Documented commands (type help <topic>):")
            for command in self.commands:
                print("\t{}".format(command))


if __name__ == "__main__":
    HBNBCommand().cmdloop()

