#!/usr/bin/python3
"""
Module for test cases for the City class
"""
import pep8
import os
import unittest
from models import city
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Unittest class for testing the City class
    """

    @classmethod
    def setUpClass(cls):
        """ Instances the City class with attribute name """
        cls.city_test = City()
        cls.city_test.name = "Providence"
        cls.city_test.state_id = "13"

    @classmethod
    def tearDownClass(cls):
        """ Removes the json file used as test when finished """
        del cls.city_test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """ Tests pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        results = pep8style.check_files(['models/city.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_documentation(self):
        """ Test if city module is documented """
        self.assertTrue(city.__doc__)

    def test_class_documentation(self):
        """ Test if City class is documented """
        self.assertTrue(City.__doc__)

    def test_if_subclass(self):
        """ Tests if City is a subclass of BaseModel """
        self.assertTrue(issubclass(self.city_test.__class__, BaseModel), True)

    def test_has_attributes(self):
        """ Test if city_test has certain attributes """
        self.assertTrue('id' in self.city_test.__dict__)
        self.assertTrue('created_at' in self.city_test.__dict__)
        self.assertTrue('updated_at' in self.city_test.__dict__)
        self.assertTrue('name' in self.city_test.__dict__)
        self.assertTrue('state_id' in self.city_test.__dict__)

    def test_attributes_are_strings(self):
        """ Test if the attributes name and state_id are type string """
        self.assertEqual(type(self.city_test.name), str)
        self.assertEqual(type(self.city_test.state_id), str)

    def test_save(self):
        """
        Test save method inherited from BaseModel by
        comparing attributes created at and updated at
        """
        self.city_test.save()
        self.assertNotEqual(self.city_test.created_at, self.city_test.updated_at)

    def test_to_dict(self):
        """ Test to_dict method inherited from BaseModel """
        self.assertEqual('to_dict' in dir(self.city_test), True)


if __name__ == "__main__":
    unittest.main()