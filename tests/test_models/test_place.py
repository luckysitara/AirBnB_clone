#!/usr/bin/python3

""" Unittest module for class Place
Test cases:
    TestPlace_init
    TestPlace_dict_method
    TestPlace_save
"""

import unittest
import os
from time import sleep
import models
from datetime import datetime
from models.place import Place


class TestPlace_init(unittest.TestCase):
    """ tests for Place class instantiation """
    def test_type(self):
        m = Place()
        self.assertEqual(type(m), Place)

    def test_public_attribute_city_id(self):
        mod = Place()
        self.assertEqual(str, type(mod.city_id))
        self.assertIn("city_id", dir(mod))
        self.assertNotIn("city_id", mod.__dict__)

    def test_public_attribute_max_guest(self):
        mod = Place()
        self.assertEqual(int, type(mod.max_guest))
        self.assertIn("max_guest", dir(mod))
        self.assertNotIn("max_guest", mod.__dict__)

    def test_public_attribute_amenity_ids(self):
        mod = Place()
        self.assertEqual(list, type(mod.amenity_ids))
        self.assertIn("amenity_ids", dir(mod))
        self.assertNotIn("amenity_ids", mod.__dict__)

    def test_public_attribute_longitude(self):
        mod = Place()
        self.assertEqual(float, type(mod.longitude))
        self.assertIn("longitude", dir(mod))
        self.assertNotIn("longitude", mod.__dict__)

    def test_id_type_is_str(self):
        mod = Place()
        self.assertEqual(str, type(mod.id))

    def test_id_for_two_models(self):
        mod1 = Place()
        mod2 = Place()
        self.assertNotEqual(mod2.id, mod1.id)

    def test_updated_at_is_date_time(self):
        mod = Place()
        self.assertEqual(datetime, type(mod.updated_at))

    def test_created_at_is_date_time(self):
        mod = Place()
        self.assertEqual(datetime, type(mod.created_at))

    def test_created_at_time_difference(self):
        mod1 = Place()
        sleep(0.07)
        mod2 = Place()
        self.assertLess(mod1.created_at, mod2.created_at)

    def test_updated_at_time_difference(self):
        mod1 = Place()
        sleep(0.07)
        mod2 = Place()
        self.assertLess(mod1.updated_at, mod2.updated_at)

    def test_kwargs(self):
        create = datetime.now()
        update = datetime.now()
        attr = {
                "id": "12345",
                "created_at": create.isoformat(),
                "updated_at": update.isoformat()
            }
        mod = Place(**attr)
        self.assertEqual(mod.id, "12345")
        self.assertEqual(mod.updated_at, update)
        self.assertEqual(mod.created_at, create)


class TestPlace_dict_method(unittest.TestCase):
    """ Test case for the dictionary method of the Place class """
    def test_return_of_is_dict(self):
        mod = Place()
        self.assertTrue(dict, type(mod.to_dict()))

    def test_dict_difference(self):
        mod = Place()
        self.assertNotEqual(mod.to_dict(), mod.__dict__)

    def test_with_args(self):
        mod = Place()
        with self.assertRaises(TypeError):
            mod.to_dict("Hello")

    def test_return_value(self):
        mod = Place()
        mod.id = "99999"
        create = datetime.now()
        update = datetime.now()
        mod.created_at = create
        mod.updated_at = update
        test_dict = {
                "id": "99999",
                "created_at": create.isoformat(),
                "updated_at": update.isoformat(),
                "__class__": "Place"
                }
        self.assertDictEqual(test_dict, mod.to_dict())

    def test_added_dict_content(self):
        mod = Place()
        mod.name = "My_first_model"
        mod.test = "first"
        mod.num = 1
        self.assertIn("num", mod.to_dict())
        self.assertIn("name", mod.to_dict())
        self.assertIn("test", mod.to_dict())

    def test_dict_keys(self):
        mod = Place()
        self.assertIn("__class__", mod.to_dict())
        self.assertIn("id", mod.to_dict())
        self.assertIn("created_at", mod.to_dict())
        self.assertIn("updated_at", mod.to_dict())

    def test_datetime_is_str(self):
        mod = Place()
        test_dict = mod.to_dict()
        self.assertEqual(str, type(test_dict["created_at"]))
        self.assertEqual(str, type(test_dict["updated_at"]))


class TestPlace_save(unittest.TestCase):
    """ Test case for Place save method """
    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_one_call(self):
        mod = Place()
        sleep(0.07)
        update = mod.updated_at
        mod.save()
        self.assertLess(update, mod.updated_at)

    def test_two_calls(self):
        mod = Place()
        sleep(0.07)
        update = mod.updated_at
        mod.save()
        self.assertLess(update, mod.updated_at)
        new_update_at = mod.updated_at
        sleep(0.07)
        mod.save()
        self.assertLess(new_update_at, mod.updated_at)

    def test_with_args(self):
        mod = Place()
        with self.assertRaises(TypeError):
            mod.save([])

    def test_file_content(self):
        mod = Place()
        mod.save()
        mod_id = "Place" + "." + mod.id
        with open("file.json", "r") as file:
            self.assertIn(mod_id, file.read())


if __name__ == '__main__':
    unittest.main()
