#!/usr/bin/python3
"""
Module for class: FileStorage
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Class that handles the storage of json strings
    """

    __file_path = "file.json"
    __objects = {}
    classes_dict = {"BaseModel": BaseModel,
                    "User": User,
                    "Amenity": Amenity,
                    "City": City,
                    "Place": Place,
                    "Review": Review,
                    "State": State}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        dictionary = {}
        if self.__objects is not None:
            for key, value in self.__objects.items():
                dictionary[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(dictionary, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file exists)
        """

        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                temp_objects = json.load(file)
            for key, value in temp_objects.items():
                self.__objects[key] = \
                    self.classes_dict[value['__class__']](**value)
        except FileNotFoundError:
            pass
