#!/usr/bin/python3

""" Unittest module for class State
Test cases:
    TestState_init
    TestState_dict_method
    TestState_save
"""

import unittest
import os
from time import sleep
import models
from datetime import datetime
from models.state import State


class TestState_init(unittest.TestCase):
    """ tests for State class instantiation """
    def test_type(self):
        m = State()
        self.assertEqual(type(m), State)

    def test_public_attribute_name(self):
        m = State()
        self.assertEqual(str, type(m.name))
        self.assertIn("name", dir(m))
        self.assertNotIn("name", m.__dict__)

    def test_id_type_is_str(self):
        mod = State()
        self.assertEqual(str, type(mod.id))

    def test_id_for_two_models(self):
        mod1 = State()
        mod2 = State()
        self.assertNotEqual(mod2.id, mod1.id)

    def test_updated_at_is_date_time(self):
        mod = State()
        self.assertEqual(datetime, type(mod.updated_at))

    def test_created_at_is_date_time(self):
        mod = State()
        self.assertEqual(datetime, type(mod.created_at))

    def test_created_at_time_difference(self):
        mod1 = State()
        sleep(0.07)
        mod2 = State()
        self.assertLess(mod1.created_at, mod2.created_at)

    def test_updated_at_time_difference(self):
        mod1 = State()
        sleep(0.07)
        mod2 = State()
        self.assertLess(mod1.updated_at, mod2.updated_at)

    def test_kwargs(self):
        create = datetime.now()
        update = datetime.now()
        attr = {
                "id": "12345",
                "created_at": create.isoformat(),
                "updated_at": update.isoformat()
            }
        mod = State(**attr)
        self.assertEqual(mod.id, "12345")
        self.assertEqual(mod.updated_at, update)
        self.assertEqual(mod.created_at, create)


class TestState_dict_method(unittest.TestCase):
    """ Test case for the dictionary method of the State class """
    def test_return_of_is_dict(self):
        mod = State()
        self.assertTrue(dict, type(mod.to_dict()))

    def test_dict_difference(self):
        mod = State()
        self.assertNotEqual(mod.to_dict(), mod.__dict__)

    def test_with_args(self):
        mod = State()
        with self.assertRaises(TypeError):
            mod.to_dict("Hello")

    def test_return_value(self):
        mod = State()
        mod.id = "99999"
        create = datetime.now()
        update = datetime.now()
        mod.created_at = create
        mod.updated_at = update
        test_dict = {
                "id": "99999",
                "created_at": create.isoformat(),
                "updated_at": update.isoformat(),
                "__class__": "State"
                }
        self.assertDictEqual(test_dict, mod.to_dict())

    def test_added_dict_content(self):
        mod = State()
        mod.name = "My_first_model"
        mod.test = "first"
        mod.num = 1
        self.assertIn("num", mod.to_dict())
        self.assertIn("name", mod.to_dict())
        self.assertIn("test", mod.to_dict())

    def test_dict_keys(self):
        mod = State()
        self.assertIn("__class__", mod.to_dict())
        self.assertIn("id", mod.to_dict())
        self.assertIn("created_at", mod.to_dict())
        self.assertIn("updated_at", mod.to_dict())

    def test_datetime_is_str(self):
        mod = State()
        test_dict = mod.to_dict()
        self.assertEqual(str, type(test_dict["created_at"]))
        self.assertEqual(str, type(test_dict["updated_at"]))


class TestState_save(unittest.TestCase):
    """ Test case for State save method """
    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_one_call(self):
        mod = State()
        sleep(0.07)
        update = mod.updated_at
        mod.save()
        self.assertLess(update, mod.updated_at)

    def test_two_calls(self):
        mod = State()
        sleep(0.07)
        update = mod.updated_at
        mod.save()
        self.assertLess(update, mod.updated_at)
        new_update_at = mod.updated_at
        sleep(0.07)
        mod.save()
        self.assertLess(new_update_at, mod.updated_at)

    def test_with_args(self):
        mod = State()
        with self.assertRaises(TypeError):
            mod.save([])

    def test_file_content(self):
        mod = State()
        mod.save()
        mod_id = "State" + "." + mod.id
        with open("file.json", "r") as file:
            self.assertIn(mod_id, file.read())


if __name__ == '__main__':
    unittest.main()
