#!/usr/bin/python3
"""
Module for test cases for the Review class
"""
import pep8
import os
import unittest
from models import review
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Unittest class for testing the Review class
    """

    @classmethod
    def setUpClass(cls):
        """ Instances the Review class with attribute name """
        cls.review_test = Review()
        cls.review_test.place_id = "Place13"
        cls.review_test.user_id = "User26"
        cls.review_test.text = "Review goes here"

    @classmethod
    def tearDownClass(cls):
        """ Removes the json file used as test when finished """
        del cls.review_test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """ Tests pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        results = pep8style.check_files(['models/review.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_documentation(self):
        """ Test if review module is documented """
        self.assertTrue(review.__doc__)

    def test_class_documentation(self):
        """ Test if Review class is documented """
        self.assertTrue(Review.__doc__)

    def test_if_subclass(self):
        """ Tests if Review is a subclass of BaseModel """
        self.assertTrue(issubclass(self.review_test.__class__, BaseModel), True)

    def test_has_attributes(self):
        """ Test if review_test has certain attributes """
        self.assertTrue('id' in self.review_test.__dict__)
        self.assertTrue('created_at' in self.review_test.__dict__)
        self.assertTrue('updated_at' in self.review_test.__dict__)
        self.assertTrue('place_id' in self.review_test.__dict__)
        self.assertTrue('user_id' in self.review_test.__dict__)
        self.assertTrue('text' in self.review_test.__dict__)

    def test_attributes_are_strings(self):
        """
        Test if the attributes place_id,
        user_id and text are type string
        """
        self.assertEqual(type(self.review_test.place_id), str)
        self.assertEqual(type(self.review_test.user_id), str)
        self.assertEqual(type(self.review_test.text), str)

    def test_save(self):
        """
        Test save method inherited from BaseModel by
        comparing attributes created at and updated at
        """
        self.review_test.save()
        self.assertNotEqual(self.review_test.created_at, self.review_test.updated_at)

    def test_to_dict(self):
        """ Test to_dict method inherited from BaseModel """
        self.assertEqual('to_dict' in dir(self.review_test), True)


if __name__ == "__main__":
    unittest.main()