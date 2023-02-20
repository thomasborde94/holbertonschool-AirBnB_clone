#!/usr/bin/python3
"""Defines a class FileStorage."""
import json
from models.base_model import BaseModel


class FileStorage():
    """Represent the class FileStorage.
    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): dictionary - empty but
        will store all objects by <class name>.id 
    """

    __file_path = file.json
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class.__name__, obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as json_file:
            json_file.write(json.dump(self.__objects)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists)"""
            try:
                with open(self.__file_path, "r") as jsonfile:
                    json_str = jsonfile.read()
                    self.__objects = json.load(json_str)
            except FileNotFoundError:
                pass
            
