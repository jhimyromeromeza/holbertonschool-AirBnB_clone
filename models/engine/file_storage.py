#!/usr/bin/python3


import os
import json
from models.base_model import BaseModel
"""The FileStorage is a class that serves  for serializing instances of objects
    to a JSON file and deserializing JSON data back to instances."""


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances

    Attr:
    __file_path: A str repre the path to the JSON file where data be stored
    __objects:  A dictionary that will store all objects by <class name>.id.
    """
    
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}
        
    def all(self, cls=None):
        """Returns a dictionary of all objects"""

        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Sets an object in the __objects attribute"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                for k, v in json.load(f).items():
                    cls_name = k.split('.')[0]
                    self.__objects[k] = eval(cls_name)(**v)
