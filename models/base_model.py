#!/usr/bin/python3
from datetime import datetime
from models import storage
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            timestamp_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, timestamp_format)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def _str_representation(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save_and_update(self):
        self.updated_at = datetime.now()
        storage.save()

    def attributes_to_custom_dict(self):
        output = self.__dict__.copy()
        output['__class__'] = self.__class__.__name__
        output['created_at'] = self.created_at.isoformat()
        output['updated_at'] = self.updated_at.isoformat()
        return output
