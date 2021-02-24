#!/usr/bin/python3
"""holberton Module"""
import models
from models.user import User
import json


class FileStorage:
    """define File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = type(obj).__name__
        key_obj = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key_obj] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                self__objects = json.load(f)
        except:
            pass
