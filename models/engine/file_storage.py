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
    __classes = {}

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
            n_dict = self.all()
            dict_serl = {}
            for key, value in n_dict.items():
                dict_serl[key] = value.to_dict()
            json.dump(dict_serl, file)

    def get_classes(self, str_id):
        """ Returns class models 
        Args:
            str_id (str): instance id to get model
        """
        from models.base_model import BaseModel
        FileStorage.__classes = {"BaseModel" : BaseModel}
        for key, value in FileStorage.__classes.items():
            if key in str_id:
                return FileStorage.__classes[key]
        

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fi:
                objects = json.loads(fi.read())
                active_class = self.all()
                for key, value in objects.items():
                    active_class[key] = self.get_classes(key)(**value)
