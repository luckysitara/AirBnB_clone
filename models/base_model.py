#!/usr/bin/python3
"""
    BaseModel class module for AirBnB_clone
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base class for the AirBnB_clone classes
    Attributes:
        id (str): id of an instance of this class
        created_at (datetime): time an imstance was created
        updated_at (datetime): time an instance of this object is updated
    """
    def __init__(self, *args, **kwargs):
        """ Initalizes an object of class Basemodel
        Args:
            args (tuple): variable lenght argument
            kwargs (dict): contains instance attributes and values
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Prints informal class representation of a Basemodel oject """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Updates public class attribute attribute updated_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        of the instance """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        if type(inst_dict["created_at"]) is datetime:
            inst_dict["created_at"] = inst_dict["created_at"].isoformat()
        if type(inst_dict["updated_at"]) is datetime:
            inst_dict["updated_at"] = inst_dict["updated_at"].isoformat()
        return inst_dict
