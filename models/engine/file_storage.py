#!/usr/bin/python3
"""
    FileStorage Class module
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to
    instances
    Attributes:
        __file_path (str): private class attribute containing a file path
        __objects (dict): contains the id of all object instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary containing all object instances id """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        Args:
            obj (BaseModel): instance of a class Basemodel
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            n_dict = self.all()
            dict_serl = {}
            for key, value in n_dict.items():
                dict_serl[key] = value.to_dict()
            json.dump(dict_serl, file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists """
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, 'r', encoding="utf-8") as fi:
                    content = fi.read()
                    if content:
                        objects_dict = json.loads(content)
                        for value in objects_dict.values():
                            cls_name = value.get("__class__")
                            if cls_name and cls_name in globals():
                                n_object = eval(cls_name)(**value)
                                self.new(n_object)
        except Exception:
            pass
