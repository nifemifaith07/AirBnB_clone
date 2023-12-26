#!/bin/usr/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent the city
    Attributes:
        state_id (str): empty string: it will be State.id
        name (str): empty string
    """
    state_id = ""
    name = ""
