#!/usr/bin/python3

""" Unittest module for class Amenity
Test cases:
    TestAmenity_init
    TestAmenity_dict_method
    TestAmenity_save
"""

import unittest
import os
from time import sleep
import models
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_init(unittest.TestCase):
    """ tests for Amenity class instantiation """
    def test_type(self):
        m = Amenity()
        self.assertEqual(type(m), Amenity)

    def test_id_type_is_str(self):
        mod = Amenity()
        self.assertEqual(str, type(mod.id))

    def test_id_for_two_models(self):
        mod1 = Amenity()
        mod2 = Amenity()
        self.assertNotEqual(mod2.id, mod1.id)

    def test_public_attributes(self):
        mod = Amenity()
        self.assertIn("name", dir(mod))
        self.assertNotIn("name", mod.__dict__)
        self.assertEqual(str, type(mod.name))

    def test_updated_at_is_date_time(self):
        mod = Amenity()
        self.assertEqual(datetime, type(mod.updated_at))

    def test_created_at_is_date_time(self):
        mod = Amenity()
        self.assertEqual(datetime, type(mod.created_at))

    def test_created_at_time_difference(self):
        mod1 = Amenity()
        sleep(0.07)
        mod2 = Amenity()
        self.assertLess(mod1.created_at, mod2.created_at)

    def test_updated_at_time_difference(self):
        mod1 = Amenity()
        sleep(0.07)
        mod2 = Amenity()
        self.assertLess(mod1.updated_at, mod2.updated_at)

    def test_kwargs(self):
        create = datetime.now()
        update = datetime.now()
        attr = {
                "id": "12345",
                "created_at": create.isoformat(),
                "updated_at": update.isoformat()
            }
        mod = Amenity(**attr)
        self.assertEqual(mod.id, "12345")
        self.assertEqual(mod.updated_at, update)
        self.assertEqual(mod.created_at, create)


class TestAmenity_dict_method(unittest.TestCase):
    """ Test case for the dictionary method of the Amenity class """
    def test_return_of_is_dict(self):
        mod = Amenity()
        self.assertTrue(dict, type(mod.to_dict()))

    def test_dict_difference(self):
        mod = Amenity()
        self.assertNotEqual(mod.to_dict(), mod.__dict__)

    def test_with_args(self):
        mod = Amenity()
        with self.assertRaises(TypeError):
            mod.to_dict("Hello")

    def test_return_value(self):
        mod = Amenity()
        mod.id = "99999"
        create = datetime.now()
        update = datetime.now()
        mod.created_at = create
        mod.updated_at = update
        test_dict = {
                "id": "99999",
                "created_at": create.isoformat(),
                "updated_at": update.isoformat(),
                "__class__": "Amenity"
                }
        self.assertDictEqual(test_dict, mod.to_dict())

    def test_added_dict_content(self):
        mod = Amenity()
        mod.name = "My_first_model"
        mod.test = "first"
        mod.num = 1
        self.assertIn("num", mod.to_dict())
        self.assertIn("name", mod.to_dict())
        self.assertIn("test", mod.to_dict())

    def test_dict_keys(self):
        mod = Amenity()
        self.assertIn("__class__", mod.to_dict())
        self.assertIn("id", mod.to_dict())
        self.assertIn("created_at", mod.to_dict())
        self.assertIn("updated_at", mod.to_dict())

    def test_datetime_is_str(self):
        mod = Amenity()
        test_dict = mod.to_dict()
        self.assertEqual(str, type(test_dict["created_at"]))
        self.assertEqual(str, type(test_dict["updated_at"]))


class TestAmenity_save(unittest.TestCase):
    """ Test case for Amenity save method """
    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_one_call(self):
        mod = Amenity()
        sleep(0.07)
        update = mod.updated_at
        mod.save()
        self.assertLess(update, mod.updated_at)

    def test_two_calls(self):
        mod = Amenity()
        sleep(0.07)
        update = mod.updated_at
        mod.save()
        self.assertLess(update, mod.updated_at)
        new_update_at = mod.updated_at
        sleep(0.07)
        mod.save()
        self.assertLess(new_update_at, mod.updated_at)

    def test_with_args(self):
        mod = Amenity()
        with self.assertRaises(TypeError):
            mod.save([])

    def test_file_content(self):
        mod = Amenity()
        mod.save()
        mod_id = "Amenity" + "." + mod.id
        with open("file.json", "r") as file:
            self.assertIn(mod_id, file.read())


if __name__ == '__main__':
    unittest.main()
