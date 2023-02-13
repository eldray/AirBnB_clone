#!/usr/bin/python3
"""Testing FileStorage class """

import json
import os
import pep8
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    Testing FileStorage class
    """
    storage = FileStorage()
    classes_dict = {"BaseModel": BaseModel,
                    "User": User,
                    "Amenity": Amenity,
                    "City": City,
                    "Place": Place,
                    "Review": Review,
                    "State": State}

    def setUp(self):
        """Testing FileStorage class """
        self.file_path = getattr(FileStorage, "_FileStorage__file_path")

    def tearDown(self):
        """Testing FileStorage class """
        setattr(FileStorage, "_FileStorage__objects", {})

    def test_style_check(self):
        """ Tests pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        results = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_documentation(self):
        """ Test if file_storage module is documented """
        self.assertTrue(file_storage.__doc__)

    def test_documentation_methods(self):
        """ Test if methods have comments"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_instance_type(self):
        """ Test instance type """
        self.assertEqual(type(self.storage.all()), dict)

    def test_type_id(self):
        """ Test id type """
        my_model = BaseModel()
        self.assertEqual(type(my_model.id), str)

    def test_types(self):
        """
        Test types
        """
        self.assertIsInstance(self.storage, FileStorage)
        self.assertIsInstance(self.storage._FileStorage__file_path, str)
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_type_created_at(self):
        """ Test types of attributes """
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.to_dict()['created_at']), str)

    def test_type_updated_at(self):
        """ Test types of attributes """
        my_model = BaseModel()
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.to_dict()['updated_at']), str)

    def test_all(self):
        """
        Tests method: all (returns dictionary <class>.<id> : <obj instance>)
        """
        test_storage = FileStorage()
        instances_dic = test_storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, test_storage._FileStorage__objects)

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
        test_storage = FileStorage()
        instances_dic = test_storage.all()
        lutia = User()
        lutia.id = 777
        lutia.name = "Lutia"
        test_storage.new(lutia)
        key = lutia.__class__.__name__ + "." + str(lutia.id)
        self.assertIsNotNone(instances_dic[key])

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        test_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(test_storage.reload(), None)

    def test_save(self):
        """ Test save method """
        my_model = BaseModel()
        prev = my_model.updated_at
        my_model.save()
        self.assertTrue(my_model.updated_at > prev)

    def test_save_serialization(self):
        """ Tests serialization of method save """
        os.remove("file.json")
        test_storage = FileStorage()
        test_dictionary = {}
        for key, value in self.classes_dict.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            test_dictionary[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = test_dictionary
        test_storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in test_dictionary.items():
            test_dictionary[key] = value.to_dict()
        string = json.dumps(test_dictionary)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))


if __name__ == "__main__":
    unittest.main()