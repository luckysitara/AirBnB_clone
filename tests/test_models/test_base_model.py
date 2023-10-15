#!/usr/bin/python3

""" Unittest module for class BaseModel
Test cases:
    TestBaseModel_init
    TestBaseModel_dict_method
    TestBaseModel_save
"""

import unittest
import os
from time import sleep
import models
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    """ tests for BaseModel class instantiation """
    def test_type(self):
        m = BaseModel()
        self.assertEqual(type(m), BaseModel)

    def test_id_type_is_str(self):
        mod = BaseModel()
        self.assertEqual(str, type(mod.id))

    def test_id_for_two_models(self):
        mod1 = BaseModel()
        mod2 = BaseModel()
        self.assertNotEqual(mod2.id, mod1.id)

    def test_updated_at_is_date_time(self):
        mod = BaseModel()
        self.assertEqual(datetime, type(mod.updated_at))

    def test_created_at_is_date_time(self):
        mod = BaseModel()
        self.assertEqual(datetime, type(mod.created_at))

    def test_created_at_time_difference(self):
        mod1 = BaseModel()
        sleep(0.07)
        mod2 = BaseModel()
        self.assertLess(mod1.created_at, mod2.created_at)

    def test_updated_at_time_difference(self):
        mod1 = BaseModel()
        sleep(0.07)
        mod2 = BaseModel()
        self.assertLess(mod1.updated_at, mod2.updated_at)

    def test_kwargs(self):
        create = datetime.now()
        update = datetime.now()
        attr = {
                "id": "12345",
                "created_at": create.isoformat(),
                "updated_at": update.isoformat()
            }
        mod = BaseModel(**attr)
        self.assertEqual(mod.id, "12345")
        self.assertEqual(mod.updated_at, update)
        self.assertEqual(mod.created_at, create)


class TestBaseModel_dict_method(unittest.TestCase):
    """ Test case for the dictionary method of the BaseModel class """
    def test_return_of_is_dict(self):
        mod = BaseModel()
        self.assertTrue(dict, type(mod.to_dict()))

    def test_dict_difference(self):
        mod = BaseModel()
        self.assertNotEqual(mod.to_dict(), mod.__dict__)

    def test_with_args(self):
        mod = BaseModel()
        with self.assertRaises(TypeError):
            mod.to_dict("Hello")

    def test_return_value(self):
        mod = BaseModel()
        mod.id = "99999"
        create = datetime.now()
        update = datetime.now()
        mod.created_at = create
        mod.updated_at = update
        test_dict = {
                "id": "99999",
                "created_at": create.isoformat(),
                "updated_at": update.isoformat(),
                "__class__": "BaseModel"
                }
        self.assertDictEqual(test_dict, mod.to_dict())

    def test_added_dict_content(self):
        mod = BaseModel()
        mod.name = "My_first_model"
        mod.test = "first"
        mod.num = 1
        self.assertIn("num", mod.to_dict())
        self.assertIn("name", mod.to_dict())
        self.assertIn("test", mod.to_dict())

    def test_dict_keys(self):
        mod = BaseModel()
        self.assertIn("__class__", mod.to_dict())
        self.assertIn("id", mod.to_dict())
        self.assertIn("created_at", mod.to_dict())
        self.assertIn("updated_at", mod.to_dict())

    def test_datetime_is_str(self):
        mod = BaseModel()
        test_dict = mod.to_dict()
        self.assertEqual(str, type(test_dict["created_at"]))
        self.assertEqual(str, type(test_dict["updated_at"]))


class TestBaseModel_save(unittest.TestCase):
    """ Test case for BaseModel save method """
    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_one_call(self):
        mod = BaseModel()
        sleep(0.07)
        update = mod.updated_at
        mod.save()
        self.assertLess(update, mod.updated_at)

    def test_two_calls(self):
        mod = BaseModel()
        sleep(0.07)
        update = mod.updated_at
        mod.save()
        self.assertLess(update, mod.updated_at)
        new_update_at = mod.updated_at
        sleep(0.07)
        mod.save()
        self.assertLess(new_update_at, mod.updated_at)

    def test_with_args(self):
        mod = BaseModel()
        with self.assertRaises(TypeError):
            mod.save([])

    def test_file_content(self):
        mod = BaseModel()
        mod.save()
        mod_id = "BaseModel" + "." + mod.id
        with open("file.json", "r") as file:
            self.assertIn(mod_id, file.read())


if __name__ == '__main__':
    unittest.main()
