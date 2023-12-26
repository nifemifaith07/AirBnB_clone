#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Represent the Review
    attributes:
        place_id (str): empty string: it will be the Place.id
        user_id (str): empty string: it will be the User.id
        text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""
