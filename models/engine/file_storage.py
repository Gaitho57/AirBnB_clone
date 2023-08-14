#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
    """

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            The dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: The object to store.
        """
        class_name = obj.__class__.__name__
        id = obj.id
        self.__objects[class_name + "." + id] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised).
        """
        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, "r") as f:
            self.__objects = json.load(f)
