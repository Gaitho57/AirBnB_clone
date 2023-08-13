#!/usr/bin/python3
import datetime
import json
from models.engine.file_storage import FileStorage


class BaseModel:

    """
    Base class for all AirBnB models.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance.
        """
        super().__init__(*args, **kwargs)
        self.id = self._generate_uuid()
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

        if not self.id:
            self.save()

    @classmethod
    def _generate_uuid(cls):
        """
        Generate a unique identifier for a new model instance.
        """
        return str(uuid4())

    def save(self):
        """
        Save the model to the file storage.
        """
        storage.new(self)
        storage.save()
        self.updated_at = datetime.datetime.utcnow()

    def to_dict(self):
        """
        Serialize the model to a dictionary.
        """
        dictionary = {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            **self.__dict__,
        }
        return dictionary

    @classmethod
    def from_dict(cls, dictionary):
        """
        Deserialize a model from a dictionary.
        """
        instance = cls()
        instance.__dict__ = dictionary
        return instance
