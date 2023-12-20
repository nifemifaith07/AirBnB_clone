#!/usr/bin/python3
"""
Defines the HBnB console, that manages the AirBnB objects.
"""

import cmd
import re  # regex
from shlex import split  # for parsing strings
import models
from models.base_model import BaseModel
from models import storage

def check_args(args):
    """check if argument is valid
    Args:
    arg (str): the string containing the arguments passed to a command
    Return: Error message if args is None or invalid class, else the argument
    """
    arg = args.split(" ")
    if len(args) == 0:
        print("**class name missing**")
    elif arg[0] not in classes:
        print(args)
        print(len(arg))
        print(len(args))
        print(arg)
        print("**class doesn't exist**")
    else:
         return arg
classes = [
        "BaseModel",
        "User",
        "Amenity",
        "Place",
        "City",
        "State",
        "Review",
]

class HBNBCommand(cmd.Cmd):
    """ Implements the hbnb command interpreter
    Attributes:
        prompt: The command prompt
    """

    prompt = "(hbnb) "
  
    cmd_list = ["create", "show", "update", "all", "destroy", "count"]

    def precmd(self, args):
        """Parse the user input"""
        if "." in args and "(" in args and ")" in args:
            clss = args.split(".")
            cmmd = clss[1].split("(")
            argl = cmmd[1].split(")")
            if clss[0] in classes and comand[0] in self.cmd_list:
                args = comand[0] + " " + cls[0] + " " + argl[0]
        return args
 
    def emptyline(self):
        """do nothing when an empty line is passed"""
        pass

    def do_EOF(self, argv):
        """Exits the program upon receiving and EOF"""
        print("")
        return True

    def do_create(self, cls_name):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        name = check_args(cls_name)
        if name:
            if len(name) == 1:
                print(eval(cls_name)().id)
                storage.save
            else:
                print("Usage: create classname")

    def do_show(self, argv):
        """Prints the string rep of an instance based on the class name and id"""
        name = check_args(argv)
        if name:
            if len(name) != 2:
                print("** instance id missing **")
            else:
                objs = storage.all()
                for _, val in objs.items():
                    object_name = val.__class__.__name__
                    object_id = val.id
                    if object_name == name[0] and object_id == name[1].strip('"'):
                        print(val)
                        return
                print("** no instance found **")
            

    def do_all(self, argv):
        """Prints all string rep of all instances based or not on the class name"""
        objs = storage.all()
        inst = []

        if not argv:
            for _, val in objs.items():
                inst.append(val.__str__())
        else:
            # If argument is provided, print instances of the specified class
            args = argv.split(" ")
            if args[0] not in classes:
                print("** class doesn't exist **")
                return

            for _, val in objs.items():
                object_name = val.__class__.__name__
                if object_name == args[0]:
                    inst.append(val.__str__())
        print(inst)

        
if __name__ == "__main__":
    HBNBCommand().cmdloop()
