#!/usr/bin/python3
"""
Module to test the Amenity class
"""

import pep8
import os
import unittest
from models import amenity
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Unittest class for testing the Amenity class
    """

    @classmethod
    def setUpClass(cls):
        """ Instances the amenity class with attribute name """
        cls.amenity_test = Amenity()
        cls.amenity_test.name = "WiFi HotSpot"

    @classmethod
    def tearDownClass(cls):
        """ Removes the json file used as test when finished """
        del cls.amenity_test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        results = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_documentation(self):
        """ Test if amenity module is documented """
        self.assertTrue(amenity.__doc__)

    def test_class_documentation(self):
        """ Test if Amenity class is documented """
        self.assertTrue(Amenity.__doc__)

    def test_if_subclass(self):
        """ Tests if Amenity is a subclass of BaseModel """
        self.assertTrue(issubclass(self.amenity_test.__class__, BaseModel), True)

    def test_has_attributes(self):
        """ Test if amenity_test has certain attributes """
        self.assertTrue('id' in self.amenity_test.__dict__)
        self.assertTrue('created_at' in self.amenity_test.__dict__)
        self.assertTrue('updated_at' in self.amenity_test.__dict__)
        self.assertTrue('name' in self.amenity_test.__dict__)

    def test_attributes_are_strings(self):
        """ Test if the attribute name is type string """
        self.assertEqual(type(self.amenity_test.name), str)

    def test_save(self):
        """
        Test save method inherited from BaseModel by
        comparing attributes created at and updated at
        """
        self.amenity_test.save()
        self.assertNotEqual(self.amenity_test.created_at, self.amenity_test.updated_at)

    def test_to_dict(self):
        """ Test to_dict method inherited from BaseModel """
        self.assertEqual('to_dict' in dir(self.amenity_test), True)


if __name__ == "__main__":
    unittest.main()