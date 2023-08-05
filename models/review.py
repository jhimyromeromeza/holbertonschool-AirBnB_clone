#!/usr/bin/python3
from models.base_model import BaseModel
"""Module for the class Review"""


class Review(BaseModel):
    """
    attr:
        place_id: a string the place id
        user_id: a string the User id
        text: the test of the review
    """
    place_id = ""
    user_id = ""
    text = ""
