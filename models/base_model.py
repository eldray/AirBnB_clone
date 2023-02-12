#!/usr/bin/python3
"""
Module for main class: BaseModel
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    Main class that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ Class Constructor """
        if kwargs and len(kwargs) != 0:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    kwargs.update({key: datetime.fromisoformat(value)})
            self.__dict__.update(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String rep of class BaseModel
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key in ("updated_at", "created_at"):
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value

        return
