#!/usr/bin/python3
"""Defines the HBnB console, that manages the AirBnB objects.
"""

import cmd
import re  # regex
from shlex import split  # for parsing strings
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Implements the hbnb command interpreter
    Attributes:
        prompt: The command prompt
    """

    prompt = "(hbnb) "
    classes =  {"BaseModel": BaseModel}
        """User": User,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "State": State,
        "Review": Review
        """

    cmd_list = ["create", "show", "update", "all", "destroy", "count"]

    def precmd(self, args):
        """Parse the user input"""
        if "." in args and "(" in args and ")" in args:
            clss = args.split(".")
            cmmd = clss[1].split("(")
            argl = cmmd[1].split(")")
            if clss[0] in self.classes and comand[0] in self.cmd_list:
                args = comand[0] + " " + cls[0] + " " + argl[0]
        return args

    def check_args(self, args):
        """check if argument is valid
        Args:
        arg (str): the string containing the arguments passed to a command
        Return: Error message if args is None or invalid class, else the argument
        """
        pass

    def emptyline(self):
        """do nothing when an empty line is passed"""
        pass

    def do_EOF(self, argv):
        """Exits the program upon receiving and EOF"""
        print("")
        return True

    def do_create(self, cls_name):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not cls_name:
            print("**class name missing**")
        elif cls_name not in self.classes:
            print("**class doesn't exist**")
        else:
            print(eval(classes[cls_name])().id)
            storage.save
            
if __name__ == "__main__":
    HBNBCommand().cmdloop()
