#!/usr/bin/python3
"""Defines the file_storage class (an abstract storage engine)"""
import json
from models.base_model 
import BaseModel
"""from models.user import User
from models.state import State
from models.city import City
from models.place import Pla
ce
from models.amenity import Amenity
from models.review import Review"""



class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances:
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = file.json
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        clsName= obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(clsName, obj.id)] = obj
