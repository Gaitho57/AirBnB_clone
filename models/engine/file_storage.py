#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        temp = {}
        for key, value in self.__objects.items():
            temp[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file_write:
            json.dump(temp, file_write)

    def reload(self):
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, "r", encoding="utf-8") as file_read:
                    temp = json.load(file_read)
                    self.__objects = {}
                    for key, value in temp.items():
                        class_name = value['__class__']
                        class_ = eval(class_name) if class_name in globals() else None
                        if class_ is not None:
                            self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
