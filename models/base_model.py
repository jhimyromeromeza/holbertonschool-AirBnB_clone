#!/usr/bin/python3
"""class BaseModel."""
import uuid
from datetime import datetime


class BaseModel:
    """Represents baseModel of the project"""
    def __init__(self, *args, **kwargs):
        if kwargs not is None:
            for key, value in kwargs.items():
                if key, value == create_at or update_at:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.create_at = datetime.now()
                    self.updated_at = datetime.now()

    def __str__(self):
        """Return the str representation of the BaseModel instance"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """Update  with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        new_dict = self.__dict__.copy()
        new_dict = dict(self.__dict__)
        new_dict["class"] = self.__class__.__name__
        new_dict["create_at"] = self.create_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
