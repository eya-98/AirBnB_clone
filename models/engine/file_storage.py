#!/usr/bin/python3
"""holberton Module"""
import json

class FileStorage:
    """define File storage class"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """ returns the dictionary __objects"""
        return self.__object

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__object[self.__class__name__ + '.' + self.id] = obj
        
    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__object, f)

    def reload(self):
        """deserializes the JSON file"""
        try :    
            with open(self.__file_path, 'r') as f:
                objects_json = json.load(f)
        except:
            pass
