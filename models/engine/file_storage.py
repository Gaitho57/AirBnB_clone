#!/usr/bin/python3
import json
import os.path
from models.base_model import BaseModel
from models.user import User

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        serialized = self._serialize()
        with open(self.__file_path, "w") as f:
            json.dump(serialized, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                serialized = json.load(f)
                self.__objects = self._deserialize(serialized)

    def _serialize(self):
        serialized = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, BaseModel) or isinstance(obj, User):
                serialized[key] = obj.to_dict()
        return serialized

    def _deserialize(self, serialized):
        deserialized = {}
        for key, value in serialized.items():
            if value['__class__'] == 'BaseModel':
                deserialized[key] = BaseModel(**value)
            elif value['__class__'] == 'User':
                deserialized[key] = User(**value)
        return deserialized
