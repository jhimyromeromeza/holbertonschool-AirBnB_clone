#!/usr/bin/python3
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

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """is a simple getter that returns the dictionary __objects"""
        return self.__objests

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        data = {}
        for k, v in self.__objects.items():
            data[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        dic_data = {}
        try:
            with open(self.__file_path, 'r') as f:
                for k, v in dic_data.items():
                    self.__objects[k] = classes[v["__class__"]](**v)
        except FileNotFoundError:
            pass
