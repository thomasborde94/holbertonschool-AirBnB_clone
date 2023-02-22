#!/usr/bin/python3
"""Defines a class FileStorage."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """Represent the class FileStorage.
    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): dictionary - empty but
        will store all objects by <class name>.id 
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists)"""
        try:
            with open(self.__file_path, "r") as jsonfile:
                json_data = json.load(jsonfile)
            for k, v in json_data.items():
                self.__objects[k] = eval(v['__class__'])(**v)
        except FileNotFoundError:
            pass
            
