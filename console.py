#!/usr/bin/python3
"""
Defines the HBnB console, that manages the AirBnB objects.
"""

import cmd
import re  # regex
from shlex import split  # for parsing strings
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

def check_args(argv):
    """check if argument is valid
    Args:
    args (str): the string containing the arguments passed to a command
    Return: Error message if args is None or invalid class, else the argument
    """
    print(argv)
    arg = argv.split(" ")
    if len(argv) == 0:
        print("** class name missing **")
    elif arg[0] not in classes:
        print("** class doesn't exist **")
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
            if clss[0] in classes and cmmd[0] in self.cmd_list:
                args = cmmd[0] + " " + clss[0] + " " + argl[0]
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
                storage.save()
            else:
                print("Usage: create <classname>")

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

    def do_destroy(self, argv):
        """
        deletes an instance based on the classname and id
        and save the change into the JSON file
        """
        arg = check_args(argv)
        if arg:
            if len(arg) != 2:
                print("** instance id missing **")
            else:
                obj = storage.all()
                for key, val in obj.items():
                    obj_name = val.__class__.__name__
                    obj_id = val.id
                    if obj_name == arg[0] and obj_id == arg[1].strip('"'):
                        del val
                        del storage._FileStorage__objects[key]
                        storage.save()
                        return
                print("** no instance found **")

    def do_update(self, argv):
        """
        Updates an instance based on the class name and id by adding or updating attribute 
        (save the change into the JSON file)
        """
        name = check_args(argv)
        print(name)
        if name:
            if len(name) < 2:
                print("** instance id missing **")
            else:
                if len(name) == 2:
                    print("** attribute name missing **")
                elif len(name) == 3:
                    print("** value missing **")
                else:
                    obj = storage.all()
                    for key, val in obj.items():
                        obj_name = val.__class__.__name__
                        obj_id = val.id
                        if obj_name == name[0] and obj_id == name[1].strip('"'):
                            setattr(val, name[2], name[3])
                            storage.save()
                            return
                    print("** no instance found **")

    def do_count(self, class_name):
        """Count the instance of a class name from file objects"""
        count = 0
        obj = storage.all()
        for key, val in obj.items():
            clss = key.split(".")
            if clss[0] == class_name:
                count = count + 1
        print(count)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
