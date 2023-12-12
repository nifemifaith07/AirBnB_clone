#!/usr/bin/python3
"""
Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_docs
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
mod_doc = models.base_model.__doc__


class TestBaseModel_docs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """set up for docstring tests"""
        cls.base_func = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_func_docs(self):
        """Test for function docstrings"""
        for func in self.base_func:
            with self.subTest(function=func):
                self.assertIsNot(func[1].__doc__, None,
                                 "{':s} method needs a docstring".format(func[0]))
                self.assertTrue(len(func[1].__doc__) > 1,
                                "{:s} method needs a docstring".format(func[0]))

    def test_mod_doc(self):
        """tests for module docstring"""
        self.assertIsNot(mod_doc, None, 
                         "base_model.py needs a docstring")
        self.assertTrue(len(mod_doc) > 1, 
                        "base_model.py needs a docstring")

    def test_cls_doc(self):
        """tests for BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, 
                         None, "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1, 
                        "BaseModel class needs a docstring")

class TestBaseModel_instantiation(unittest.TestCase):
    """testing instantiation of the BaseModel class"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_args_stored_in_obj(self):
        self.assertIn(BaseModel(), model.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_is_unique(self):
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertLess(b1.created_at, b2.created_at)
        self.assertLess(b1.updated_at, b2.updated_at)

    def test_none(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_str_rep(self):
        dt = datetime.now()
        dt_rep = repr(dt)
        b1 = BaseModel()
        b1.id = "123456"
        b1.created_at = b1.updated_at = dt
        b1_str = b1.__str__()
        self.assertIn("[BaseModel] (123456)", b1_str)
        self.assertIn("'id': '123456'", b1_str)
        self.assertIn("'created_at': " + dt_repr, b1_str)
        self.assertIn("'updated_at': " + dt_repr, b1_str)
        
        
        
class TestBaseModel_save(unittest, TestCase)

class TestBaseModel_to_dict(unittest, TestCase)
