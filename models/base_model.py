#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage  # Import the storage variable

class BaseModel:
    """
    Base class for other models.
    Attributes: id, created_at, updated_at...
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance.

        Args:
            *args: Unused.
            **kwargs: Keyword arguments to initialize the instance with.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs.items():
            setattr(self, key, value)

        # Call new(self) method on storage for new instances
        if not kwargs:
            storage.new(self)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()  # Call save(self) method of storage

    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        """
        dict_data = dict(
            (key, value)
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        )
        dict_data["__class__"] = self.__class__.__name__
        dict_data["created_at"] = self.created_at.isoformat()
        dict_data["updated_at"] = self.updated_at.isoformat()
        return dict_data

    def __str__(self):
        """
        Return a string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
