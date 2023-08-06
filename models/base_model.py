#!/usr/bin/python3
"""class BaseModel."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Represents baseModel of the project"""
    def __init__(self, *args, **kwargs):
        dtform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    formobj = datetime.strptime(value, dtform)
                if key != "__class__":
                    setattr(self, key, value)
        else:i
            models.storage.new(self)

    def __str__(self):
        """Return the str representation of the BaseModel instance"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """Update  with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        new_dict = self.__dict__.copy()
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
