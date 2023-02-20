#!/usr/bin/python3
"""Defines the class Basemodel"""
import datetime
import uuid


class BaseModel:
    """Represent the base model.
    Attributes:
        id:
        created_at
        updated_at
    """
    
    def __init__(self, id=None, created_at=None, updated_at=None):
        """The constructor of the BaseModel Class"""
        id = str(uuid.uuid4())
        self.id = id

        created_at = datetime.datetime.now()
        self.created_at = created_at

        updated_at = datetime.datetime.now()
        self.updated_at = updated_at

    def __str__(self):
        """Return string representation of the BaseModel class"""
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        my_dict = self.__dict__
        for keys, values in my_dict.items():
            if type(my_dict[keys]) == datetime.datetime:
                my_dict[keys] = values.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return(my_dict)

        

