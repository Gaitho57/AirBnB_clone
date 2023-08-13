#!/usr/bin/python3
import json
import os.path

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump({key: value.to_dict() for key, value in self.__objects.items()}, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                json_dict = json.load(f)
                from models.base_model import BaseModel
                for key, value in json_dict.items():
                    self.__objects[key] = BaseModel(**value)
