#!/usr/bin/python3
"""Defines the HBnB console, that manages the AirBnB objects.
"""

import cmd
import re  # regex
from shlex import split  # for parsing strings


class HBNBCommand(cmd.Cmd):
    """ Implements the hbnb command interpreter
    Attributes:
        prompt: The command prompt
    """

    prompt = "(hbnb) "
    classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    ]

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

    def emptyline(self):
        """do nothing when an empty line is passed"""
        pass

    def do_EOF(self, argv):
        """Exits the program upon receiving and EOF"""
        print("")
        return True

    


if __name__ == "__main__":
    HBNBCommand().cmd
  loop()
