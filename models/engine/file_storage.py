import json
from models.base_model import BaseModel  # Add necessary imports here

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = globals()[class_name]
                    obj = cls(**value)
                    FileStorage.new(obj)  # Use FileStorage.new() instead of self.new()
        except FileNotFoundError:
            pass
