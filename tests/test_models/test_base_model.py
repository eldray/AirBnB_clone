#!/usr/bin/python3
"""
Module to test the BaseModel class
"""

import pep8
import os
import unittest
from datetime import datetime
from models import base_model
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Unittest class for testing the BaseModel class
    """

    @classmethod
    def setUpClass(cls):
        """ Instances the BaseModel class with attribute name """
        cls.base_model_test = BaseModel()
        cls.base_model_test.name = "Renata"
        cls.base_model_test.my_number = 27

    @classmethod
    def tearDownClass(cls):
        """ Removes the json file used as test when finished """
        del cls.base_model_test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """ Tests pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        results = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_documentation(self):
        """ Test if base_model module is documented """
        self.assertTrue(base_model.__doc__)

    def test_class_documentation(self):
        """ Test if BaseModel class is documented """
        self.assertTrue(BaseModel.__doc__)

    def test_class(self):
        """ Tests if BaseModel is a class """
        self.assertEqual(type(BaseModel()), BaseModel)

    def test_documentation_methods(self):
        """ Test if methods have comments"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_id(self):
        """ Test if id exists and it's type """
        self.assertTrue(self.base_model_test.id)
        self.assertEqual(type(self.base_model_test.id), str)

    def test_has_attributes(self):
        """ Test if place_test has certain attributes """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_save(self):
        """
        Test save method by comparing attributes
        created at and updated at
        """
        self.base_model_test.save()
        self.assertNotEqual(self.base_model_test.created_at, self.base_model_test.updated_at)
        self.assertIsInstance(self.base_model_test.created_at, datetime)
        self.assertIsInstance(self.base_model_test.updated_at, datetime)

    def test_updated_value_afterSave(self):
        """ Test that update is saving correct times """
        updated_pre = self.base_model_test.updated_at
        self.base_model_test.save()
        self.assertTrue(self.base_model_test.updated_at > updated_pre)

    def test_to_dict(self):
        """ Test to_dict method inherited from BaseModel """
        test_base_model_dict = self.base_model_test.to_dict()
        self.assertEqual(self.base_model_test.__class__.__name__,
                         'BaseModel')
        self.assertIsInstance(test_base_model_dict['created_at'], str)
        self.assertIsInstance(test_base_model_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
