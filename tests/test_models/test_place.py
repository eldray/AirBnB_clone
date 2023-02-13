#!/usr/bin/python3
"""
Module for test cases for the Place class
"""
import pep8
import os
import unittest
from models import place
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Unittest class for testing the Place class
    """

    @classmethod
    def setUpClass(cls):
        """ Instances the Review class with attribute name """
        cls.place_test = Place()
        cls.place_test.city_id = "City13"
        cls.place_test.user_id = "User26"
        cls.place_test.name = "AirBnb Name"
        cls.place_test.description = "Cabin by the beach"
        cls.place_test.number_rooms = 2
        cls.place_test.number_bathrooms = 2
        cls.place_test.max_guest = 5
        cls.place_test.price_by_night = 30
        cls.place_test.latitude = 41.8240
        cls.place_test.longitude = 71.4128
        cls.place_test.amenity_ids = ["TVs", "AC", "Cleaning service", "Heating"]

    @classmethod
    def tearDownClass(cls):
        """ Removes the json file used as test when finished """
        del cls.place_test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """ Tests pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        results = pep8style.check_files(['models/place.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_documentation(self):
        """ Test if place module is documented """
        self.assertTrue(place.__doc__)

    def test_class_documentation(self):
        """ Test if Place class is documented """
        self.assertTrue(Place.__doc__)

    def test_if_subclass(self):
        """ Tests if Place is a subclass of BaseModel """
        self.assertTrue(issubclass(self.place_test.__class__, BaseModel), True)

    def test_has_attributes(self):
        """ Test if place_test has certain attributes """
        self.assertTrue('id' in self.place_test.__dict__)
        self.assertTrue('created_at' in self.place_test.__dict__)
        self.assertTrue('updated_at' in self.place_test.__dict__)
        self.assertTrue('city_id' in self.place_test.__dict__)
        self.assertTrue('user_id' in self.place_test.__dict__)
        self.assertTrue('name' in self.place_test.__dict__)
        self.assertTrue('description' in self.place_test.__dict__)
        self.assertTrue('number_rooms' in self.place_test.__dict__)
        self.assertTrue('number_bathrooms' in self.place_test.__dict__)
        self.assertTrue('max_guest' in self.place_test.__dict__)
        self.assertTrue('price_by_night' in self.place_test.__dict__)
        self.assertTrue('latitude' in self.place_test.__dict__)
        self.assertTrue('longitude' in self.place_test.__dict__)
        self.assertTrue('amenity_ids' in self.place_test.__dict__)

    def test_attributes_are_strings(self):
        """
        Test if the attributes place_id,
        user_id and text are type string
        """
        self.assertEqual(type(self.place_test.city_id), str)
        self.assertEqual(type(self.place_test.user_id), str)
        self.assertEqual(type(self.place_test.name), str)
        self.assertEqual(type(self.place_test.description), str)
        self.assertEqual(type(self.place_test.number_rooms), int)
        self.assertEqual(type(self.place_test.number_bathrooms), int)
        self.assertEqual(type(self.place_test.max_guest), int)
        self.assertEqual(type(self.place_test.price_by_night), int)
        self.assertEqual(type(self.place_test.latitude), float)
        self.assertEqual(type(self.place_test.longitude), float)
        self.assertEqual(type(self.place_test.amenity_ids), list)

    def test_save(self):
        """
        Test save method inherited from BaseModel by
        comparing attributes created at and updated at
        """
        self.place_test.save()
        self.assertNotEqual(self.place_test.created_at, self.place_test.updated_at)

    def test_to_dict(self):
        """ Test to_dict method inherited from BaseModel """
        self.assertEqual('to_dict' in dir(self.place_test), True)


if __name__ == "__main__":
    unittest.main()