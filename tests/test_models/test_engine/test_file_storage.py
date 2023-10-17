#!/usr/bin/python3
""" Unittest cases for AirBnb_clone file_storage module

Test cases:
    TestFileStorage_init
    TestFileStorage_class_methods
"""

import unittest
import json
import os
import models
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_init(unittest.TestCase):
    """ Testcase for FileStorage class initialization """
    def test_FileStorage_type(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_FileStorage_file_path_type(self):
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_storage_insatnce(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_object_type(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorage_class_methods(unittest.TestCase):
    """ Testcase for FileStorage class Methods """
    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_raturn_type(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_instances(self):
        mod = BaseModel()
        models.storage.new(mod)
        self.assertIn(mod, models.storage.all().values())
        self.assertIn("BaseModel" + "." + mod.id, models.storage.all().keys())

    def test_call_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), "Hello")

    def test_save_method(self):
        mod = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.save()
        with open("file.json", "r") as file:
            json = file.read()
            self.assertIn("BaseModel." + mod.id, json)
            self.assertIn("User" + "." + user.id, json)
            self.assertIn("State" + "." + state.id, json)
            self.assertIn("Place" + "." + place.id, json)
            self.assertIn("City" + "." + city.id, json)
            self.assertIn("Amenity" + "." + amenity.id, json)
            self.assertIn("Review" + "." + review.id, json)

    def test_reload(self):
        mod = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.save()
        models.storage.reload()
        instance = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + mod.id, instance)
        self.assertIn("User" + "." + user.id, instance)
        self.assertIn("State" + "." + state.id, instance)
        self.assertIn("Place" + "." + place.id, instance)
        self.assertIn("City" + "." + city.id, instance)
        self.assertIn("Amenity" + "." + amenity.id, instance)
        self.assertIn("Review" + "." + review.id, instance)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(1)


if __name__ == "__main__":
    unittest.main()
