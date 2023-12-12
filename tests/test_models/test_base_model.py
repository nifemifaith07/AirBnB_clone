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

    def test_instantiation_with_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

        dt = datetime.now()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="3456", created__at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "3456")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_args_kwargs(self):
        dt  = datetime.now()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="3456", created__at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "3456")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)
        
class TestBaseModel_save(unittest, TestCase):
    """testing save method of the BaseModel class"""
    
    @classmethod
    def setUp(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

        @classmethod
    def tearDown(cls)
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save(self):
        bm =BaseModel()
        sleep(0.05)
        first_update = bm.updated_at
        bm.save()
        self.assertLess(first_update, bm.updated_at)
        second_update = bm.updated_at
        sleep(0.05)
        bm.save()
        self.assertLess(second_update, bm.updated_at)

    def test_save_with_args(self):
        bm =BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm =BaseModel()
        bm.save()
        bm_id = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bm_id, f.read())
        
class TestBaseModel_to_dict(unittest, TestCase):
    """testing for to_dict method of BaseModel class"""

    def test_to_dict_typr(self):
         bm =BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_content(self):
        bm =BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())
    
