#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
Base class for other models.
Attributes:
id: string - uniquely identifies instances of the BaseModel class.
created_at: represents the time&date when instance was created.
updated_at: represens the time&date when instance was last-updtd.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance.

        Args:
            *args: Unused.
            **kwargs: Keyword arguments to initialize the instance with.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
