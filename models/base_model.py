#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for other models.
    Attributes:
id: string - uniquely identifies each instance of the BaseModel class.
created_at: datetime - assign with the current datetime when an instance is createdupdated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not empty:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))

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
