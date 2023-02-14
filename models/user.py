#!/usr/bin/python3
"""
Module for class: User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User that inherits from BaseModel

    Attributes:
    email(str): The email of the user
    passord(str): The password of the user
    first_name(str): The first name of user
    last_name(str): The last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
