#!/usr/bin/python3
"""Defines the HBnB console, that manages the AirBnB objects.
"""

import cmd
import re #regex
from shlex import split #for parsing strings


class HBNBCommand(cmd.Cmd):
    """ Implements the hbnb command interpreter
    Attributes:
        prompt: The command prompt
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """do nothing when an empty line is passed"""
        pass

    def do_EOF(self, argv):
        """Exits the program upon receiving and EOF"""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
