iimport json
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
            json.dump(self.__objects, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
