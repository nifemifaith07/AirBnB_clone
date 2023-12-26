#!/usr/bin/python3
"""defines the BaseModel of the HBnB project"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initializes the BaseModel class
        Attributes:
            id(optional, str): unique id for each BaseModel
            created_at(optional, datetime): when an instance is created
            updated_at(optional, datetime):when an instan ce is modified
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(kwargs[key], t_format)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """return the string representation of BaseModel object"""
        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)

    def save(self):
        """updates the 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dict containing all keys/values of __dict__ of the instance
        only instance attributes set will be returned
        key __class__ is added to this dict with the classname of the obj
        created_at & updated_at must be converted to string obj(ISO format)
        """
        r_dict = self.__dict__.copy()
        r_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                r_dict[key] = self.__dict__[key].isoformat()
        return r_dict
