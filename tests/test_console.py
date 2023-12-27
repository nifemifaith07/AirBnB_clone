#!/usr/bin/python3
"""module to test the console/ TestCommand"""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestCommand(unittest.TestCase):

    """a class for tests re: HBNBCommand console"""

    attribute_values = {
        str: "shakedown1979",
        int: 1008,
        float: 1.08
    }

    reset_values = {
        str: "",
        int: 0,
        float: 0.0
    }

    test_random_attributes = {
        "school": "holberton",
        "mission": 972,
        "float": 9.8
    }

    def setUp(self):
        """set up for our tests"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """start fresh with storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """tear it all down"""
        pass

    def test_no_help_count(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        string = '*** No help on count\n'
        self.assertEqual(string, f.getvalue())

    def test_help(self):
        """help test in console"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            string = "\nDocumented commands (type help <topic>):" + "\n"
            string += "========================================" + "\n"
            string += "EOF  all  create  destroy  help  quit  show  update\n\n"
        self.assertEqual(string, f.getvalue())

    def test_help_EOF(self):
        """help command, EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        string = 'End-of-file input exits console.\n\n'
        self.assertEqual(string, f.getvalue())

    def test_help_quit(self):
        """test for help quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        string = 'Quit command to exit the program\n\n'
        self.assertEqual(string, f.getvalue())

    def test_help_create(self):
        """help create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        string = 'Creates a new instance.\n\n'
        self.assertEqual(string, f.getvalue())

    def test_help_show(self):
        """test help show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        string = 'Prints an instance by id.\n\n'
        self.assertEqual(string, f.getvalue())

    def test_help_destroy(self):
        """a test for help destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        s = 'Deletes an instance based on the class name and id.\n\n'
        self.assertEqual(s, f.getvalue())

    def test_help_all(self):
        """test for help all"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        s = 'Displays all instances, display all of a class of instances.\n\n'
        self.assertEqual(s, f.getvalue())

    def test_help_update(self):
        """test for help update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        string = 'Update an instance based on class name and id.\n\n'
        self.assertEqual(string, f.getvalue())

    def test_junkentry(self):
        """ enter a non-command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("yoyoyo")
        string = ""
        self.assertEqual(string, f.getvalue())

    def test_quit(self):
        """test for quitting"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    def test_EOF(self):
        """test for using EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    def test_empty(self):
        """empty line should print newline"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        string = ""
        self.assertEqual(string, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
        string = ""
        self.assertEqual(string, f.getvalue())

    def tool_test_do_create(self, classname):
        """tool to run tests on create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        key = "{}.{}".format(classname, uid)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(classname))
        self.assertTrue(uid in f.getvalue())

    def test_do_create(self):
        """test using the create command in console"""
        for classname in self.classes():
            self.tool_test_do_create(classname)

    def test_do_create_errs(self):
        """this docstring does not have a frackin syntax error"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create ruckus")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def tool_test_do_show(self, classname):
        """Helps test the show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show {} {}".format(classname, uid))
        string = f.getvalue()[:-1]
        self.assertTrue(uid in string)

    def test_do_show(self):
        """a test for show"""
        for classname in self.classes():
            self.tool_test_do_show(classname)
            self.tool_test_show_adv(classname)

    def test_do_show_error(self):
        """Tests show command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show garbage")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 6524359")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

    def tool_test_show_adv(self, classname):
        """help tool for show advanced """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        string = f.getvalue()
        self.assertTrue(uid in string)

    def test_do_show_error_adv(self):
        """test the show command upon error"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".show()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage.show()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show("6524359")')
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

    def test_do_destroy(self):
        """let's test destroy!!!"""
        for classname in self.classes():
            self.tool_test_do_destroy(classname)
            self.tool_test_destroy_adv(classname)

    def tool_test_do_destroy(self, classname):
        """a tool to help with testing destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy {} {}".format(classname, uid))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(uid in f.getvalue())

    def test_do_destroy_err(self):
        """destroy woth errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy thepatriarchy")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 8675309")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

    def test_destroy_ids(self):
        """destroy ids for every class"""
        for classname in self.classes().items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(classname))
            uid = f.getvalue()[:-1]
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('{}.destroy("{}")'.format(classname, uid))
            key = "{}.{}".format(classname, uid)
            self.assertNotIn(key, storage.all().keys())

    def test_destroy_ids_adv(self):
        """more destroy ids"""
        for classname in self.classes().items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(classname))
            uid = f.getvalue()[:-1]
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('destroy {} {}'.format(classname, uid))
            key = "{}.{}".format(classname, uid)
            self.assertNotIn(key, storage.all().keys())

    def tool_test_destroy_adv(self, classname):
        """a tool to test destroy further"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.destroy("{}")'.format(classname, uid))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(uid in f.getvalue())

    def test_do_destroy_err_adv(self):
        """test errors with destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("patriarchy.destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.destroy("8675309")')
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

    def test_do_all(self):
        """all tests all the time"""
        for classname in self.classes():
            self.tool_test_do_all(classname)
            self.tool_test_all_adv(classname)

    def tool_test_do_all(self, classname):
        """a tool to test all"""
        uid = self.create_class(classname)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertIn(uid, s)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(classname))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertIn(uid, s)

    def test_do_all_err(self):
        """all with errors and stuff"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all apologies")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def tool_test_all_adv(self, classname):
        """a tool to help test all further"""
        uid = self.create_class(classname)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.all()".format(classname))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertIn(uid, s)

    def test_do_all_error_adv(self):
        """all with errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("allin.all()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def test_count_all(self):
        """Tests count for all classes."""
        for classname in self.classes():
            self.tool_test_count_adv(classname)

    def tool_test_count_adv(self, classname):
        """ count works differently according to Zac"""
        for i in range(20):
            uid = self.create_class(classname)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.count()".format(classname))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertEqual(s, "20")

    def test_do_count_error(self):
        """ see what happens when count has errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("dracula.count()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".count()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

    def test_1_update(self):
        """let's update some instances"""
        classname = "BaseModel"
        attr = "junk"
        val = "in the trunk"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_2_update(self):
        """more updating for funsies"""
        classname = "User"
        attr = "Unittesting"
        val = "is killing me"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        string = f.getvalue()
        self.assertEqual(len(string), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        string = f.getvalue()
        self.assertIn(attr, string)
        self.assertIn(val, string)

    def test_3_update(self):
        """yet more updating"""
        classname = "City"
        attr = "Berkeley"
        val = "California"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_4_update(self):
        """ok maybe i'm going overboard here"""
        classname = "State"
        attr = "California"
        val = "The Golden State"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_5_update(self):
        """let's test amenity """
        classname = "Amenity"
        attr = "what"
        val = "is an amenity"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_6_update(self):
        """might as well do them all"""
        classname = "Review"
        attr = "gimme"
        val = "thereviews"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_7_update(self):
        """now place"""
        classname = "Place"
        attr = "boring"
        val = "tests"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_update_junk(self):
        """test it all at once baby"""
        for classname, cls in self.classes().items():
            uid = self.create_class(classname)
            for attr, value in self.test_random_attributes.items():
                if type(value) is not str:
                    pass
                quotes = (type(value) == str)
                self.tool_test_update(classname, uid, attr,
                                      value, quotes, False)
                self.tool_test_update(classname, uid, attr,
                                      value, quotes, True)
            pass
            if classname == "BaseModel":
                continue
            for attr, attr_type in self.attributes()[classname].items():
                if attr_type not in (str, int, float):
                    continue
                self.tool_test_update(classname, uid, attr,
                                      self.attribute_values[attr_type],
                                      True, False)
                self.tool_test_update(classname, uid, attr,
                                      self.attribute_values[attr_type],
                                      False, True)

    def tool_test_update(self, classname, uid, attr, val, quotes, func):
        """useful stuff here"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile("file.json"):
            os.remove("file.json")
        uid = self.create_class(classname)
        value_str = ('"{}"' if quotes else '{}').format(val)
        if func:
            cmd = '{}.update("{}", "{}", {})'
        else:
            cmd = 'update {} {} {} {}'
        cmd = cmd.format(classname, uid, attr, value_str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        msg = f.getvalue()[:-1]
        self.assertEqual(len(msg), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(str(val), s)
        self.assertIn(attr, s)

    def test_do_update_err(self):
        """test updating errors"""
        uid = self.create_class("BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update windows")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 8675309")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel {}'.format(uid))
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel {} name'.format(uid))
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** value missing **")

    def test_do_update_err_adv(self):
        """more update errors"""
        uid = self.create_class("BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".update()")
        msg = f.getvalue()[:-1]

        self.assertEqual(msg, "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("windows.update()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update('8675309')")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("{}")'.format(uid))
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("{}", "name")'.format(uid))
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** value missing **")

    def create_class(self, classname):
        """create a class when we need it"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        return uid

    def tool_load_dict(self, rep):
        """a tool to help load the dicts"""
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(rep)
        self.assertIsNotNone(res)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        dicts = json.loads(s.replace("'", '"'))
        return dicts

    def classes(self):
        """ do get our list of valid classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """helps get our attributes for testing"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
                     {"place_id": str,
                      "user_id": str,
                      "text": str}
        }
        return attributes


if __name__ == "__main__":
    unittest.main()
