import os
import json
from cmd import Cmd
from models import BaseModel


class Console(Cmd):
    """Console for managing models."""

    def __init__(self):
        super().__init__()
        self.prompt = ">>> "
        self.models = BaseModel.all()

    def do_create(self, args):
        """Creates a new instance of BaseModel."""
        if not args:
            print("** class name missing **")
            return

        class_name = args.split(" ")[0]
        if not hasattr(BaseModel, class_name):
            print("** class doesn't exist **")
            return

        model = BaseModel(class_name=class_name)
        model.save()
        print(model.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
        if not args:
            print("** instance id missing **")
            return

        args = args.split(" ")
        class_name = args[0]
        id = args[1]

        if not hasattr(BaseModel, class_name):
            print("** class doesn't exist **")
            return

        model = BaseModel.get(class_name, id)
        if not model:
            print("** no instance found **")
            return

        print(model)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return

        args = args.split(" ")
        class_name = args[0]
        id = args[1]

        if not hasattr(BaseModel, class_name):
            print("** class doesn't exist **")
            return

        model = BaseModel.get(class_name, id)
        if not model:
            print("** no instance found **")
            return

        model.delete()

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        if not args:
            models = BaseModel.all()
        else:
            class_name = args
            models = BaseModel.all(class_name)

        if not models:
            print("** no instances found **")
            return

        for model in models:
            print(model)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        if not args:
            print("** class name missing **")
            return

        args = args.split(" ")
        class_name = args[0]
        id = args[1]
        attribute = args[2]
        value = args[3]

        if not hasattr(BaseModel, class_name):
            print("** class doesn't exist **")
            return

        model = BaseModel.get(class_name, id)
        if not model:
            print("** no instance found **")
            return

        if attribute == "created_at" or attribute == "updated_at":
            print("** attribute can't be updated **")
            return

        try:
            setattr(model, attribute, value)
            model.save()
        except ValueError:
            print("** value missing **")

    def do_EOF(self, args):
        """Exits the console."""
        print("Exiting...")
        exit()


if __name__ == "__main__":
    console = Console()
    console.cmdloop()
