#!/usr/bin/python3
"""class BaseModel."""


import uuid
from datetime import datetime


class BaseModel:
    """metodo de instancia Basemodel"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict = dict(self.__dict__)
        new_dict["class"] = self.__class__.__name__
        new_dict["create_at"]= self.create_at.isoformat()
        new_dict["updated_at"]= self.updated_at.isoformat()
        return new_dict

