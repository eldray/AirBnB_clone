#!/usr/bin/python3
"""
Module for test cases for the State class
"""

import pep8
import os
import unittest
from models import state
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Unittest class for testing the State class
    """

    @classmethod
    def setUpClass(cls):
        """ Instances the State class with attribute name """
        cls.state_test = State()
        cls.state_test.name = "Rhode Island"

    @classmethod
    def tearDownClass(cls):
        """ Removes the json file used as test when finished """
        del cls.state_test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """ Tests pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        results = pep8style.check_files(['models/state.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_documentation(self):
        """ Test if state module is documented """
        self.assertTrue(state.__doc__)

    def test_class_documentation(self):
        """ Test if State class is documented """
        self.assertTrue(State.__doc__)

    def test_if_subclass(self):
        """ Tests if State is a subclass of BaseModel """
        self.assertTrue(issubclass(self.state_test.__class__, BaseModel), True)

    def test_has_attributes(self):
        """ Test if state_test has certain attributes """
        self.assertTrue('id' in self.state_test.__dict__)
        self.assertTrue('created_at' in self.state_test.__dict__)
        self.assertTrue('updated_at' in self.state_test.__dict__)
        self.assertTrue('name' in self.state_test.__dict__)

    def test_attributes_are_strings(self):
        """ Test if the attribute name is type string """
        self.assertEqual(type(self.state_test.name), str)

    def test_save(self):
        """
        Test save method inherited from BaseModel by
        comparing attributes created at and updated at
        """
        self.state_test.save()
        self.assertNotEqual(self.state_test.created_at, self.state_test.updated_at)

    def test_to_dict(self):
        """ Test to_dict method inherited from BaseModel """
        self.assertEqual('to_dict' in dir(self.state_test), True)


if __name__ == "__main__":
    unittest.main()