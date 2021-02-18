#!/usr/bin/python3
"""Holberton Module"""
import uuid
import models
from models import storage
from datetime import datetime
forma = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """instantiation of attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs["created_at"], forma)
            self.updated_at = datetime.strptime(kwargs["updated_at"], forma)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
            storage.save()

    def __str__(self):
        """print the id and the dict"""
        return ("[{}], ({}), {}".format(self.__class__.__name__,
                                        self.id, self.__dict__))

    def save(self):
        """
        updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['updated_at'] = self.updated_at.isoformat()
        dic['created_at'] = self.created_at.isoformat()
        return dic
