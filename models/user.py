#!/usr/bin/python3
from models.base_model import BaseModel
"""Module for class User"""


class User(BaseModel):
    """
    class User that inherits from BaseModel
    attributes:
    email : email of user
    password: password of User
    first_name: first name of User
    last_name: last name of User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
