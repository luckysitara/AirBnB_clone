#!/usr/bin/python3
"""
    FileStorage Class module
"""

import os
import json


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
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        Args:
            obj (BaseModel): instance of a class Basemodel
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            n_dict = dict(FileStorage.__objects)
            for key, value in n_dict.items():
                n_dict[key] = value.to_dict()
            json.dump(n_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fi:
                FileStorage.__objects = json.loads(fi.read())
