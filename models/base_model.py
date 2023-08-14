#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    Base class for other models.
    Attributes:
        id: string uniquely ids each instance of the BaseModel class.
        created_at: datetime object represents the time&date when instance was created.
        updated_at: datetime object represents the time&date when instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance.

        Args:
            **kwargs: Keyword arguments to initialize the instance with.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs.items():
            setattr(self, key, value)

        if kwargs:
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of the instance.

        Returns:
            A string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.

        Returns:
            A dictionary representation of the instance.
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
