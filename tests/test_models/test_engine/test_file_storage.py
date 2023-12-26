#!/usr/bin/python3
"""Test Suite for FileStorage in models/file_storage.py"""
import os.path
import unittest
import models
from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class TestFileStorage(unittest.TestCase):
    """tests for the FileStorage class
    be advised:
        rat ususally means an instance of an object"""

    def setUp(self):
        """set up"""
        pass

    def resetStorage(self):
        """start fresh with FileStorage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """tear it down"""
        self.resetStorage()
        pass

    def test_instantiation(self):
        """make an instance of storage class"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_no_args(self):
        """no args please"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_init_such_args(self):
        """such args much wow"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            rat = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "object() takes no parameters"
        self.assertEqual(str(e.exception), msg)

    def test_class_attributes(self):
        """classy attributes you got there"""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})
        

class TestFileStorageInit(unittest.TestCase):
    """Contains test cases against the FileStorage initialization"""

    def test_file_path_is_a_private_class_attr(self):
        """Checks that file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """Checks that objects is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_without_arg(self):
        """Tests initialization without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Tests initialization with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """Tests storage created in __init__.py"""
        self.assertEqual(type(models.storage), FileStorage)


class TestStorageMethods(unittest.TestCase):
    """Contains test cases against the methods present in FileStorage"""

    @classmethod
    def setUp(self):
        """Code to execute before testing occurs"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Code to execute after tests are executed"""
        # Remove file.json if it exists
        try:
            os.remove("file.json")
        except IOError:
            pass

        # rename tmp.json from setUp() to file.json
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Tests all() method of the FileStorage class"""
        self.assertTrue(type(models.storage.all()) is dict)

        # What if arg is passed? Ohh! TypeError, do your job!
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        """Tests the new() method of the FileStorage class"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        # Checks that the objects created above are stored already
        self.assertIn("BaseModel." + dummy_bm.id,
                      models.storage.all().keys())
        self.assertIn(dummy_bm, models.storage.all().values())
        self.assertIn("User." + dummy_user.id, models.storage.all().keys())
        self.assertIn(dummy_user, models.storage.all().values())
        self.assertIn("State." + dummy_state.id, models.storage.all().keys())
        self.assertIn(dummy_state, models.storage.all().values())
        self.assertIn("Place." + dummy_place.id, models.storage.all().keys())
        self.assertIn(dummy_place, models.storage.all().values())
        self.assertIn("City." + dummy_city.id, models.storage.all().keys())
        self.assertIn(dummy_city, models.storage.all().values())
        self.assertIn("Amenity." + dummy_amenity.id,
                      models.storage.all().keys())
        self.assertIn(dummy_amenity, models.storage.all().values())
        self.assertIn("Review." + dummy_review.id,
                      models.storage.all().keys())
        self.assertIn(dummy_review, models.storage.all().values())
        # What if more than one arg were passed to this guy?
        # TypeError, we need you here!
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

        # What if None was passed? That guy needs learn a lesson...
        # AttributeError, will you join us?
        with self.assertRaises(AttributeError):
            models.storage.new(None)
        

    def test_save_method(self):
        """Time to deal with reload() method in FileStorage class"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        models.storage.save()

        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + dummy_bm.id, save_text)
            self.assertIn("User." + dummy_user.id, save_text)
            self.assertIn("State." + dummy_state.id, save_text)
            self.assertIn("Place." + dummy_place.id, save_text)
            self.assertIn("City." + dummy_city.id, save_text)
            self.assertIn("Amenity." + dummy_amenity.id, save_text)
            self.assertIn("Review." + dummy_review.id, save_text)

        # What happens when an arg is passed? TypeError has been my agent!
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method(self):
        """Tests the reload method... Quite tricky!"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + dummy_bm.id, objects)
        self.assertIn("User." + dummy_user.id, objects)
        self.assertIn("State." + dummy_state.id, objects)
        self.assertIn("Place." + dummy_place.id, objects)
        self.assertIn("City." + dummy_city.id, objects)
        self.assertIn("Amenity." + dummy_amenity.id, objects)
        self.assertIn("Review." + dummy_review.id, objects)
        # What happens when an arg is passed? TypeError is raised
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
