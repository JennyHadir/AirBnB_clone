#!/usr/bin/python3
""" The entry point of the command interpreter """

import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage

cls_list = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit the console
        """
        return True

    do_EOF = do_quit

    def emptyline(self):
        """Do nothing when line is empty"""
        pass

    def do_create(self, line):
        """ Create a new instance of class
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line in cls_list:
                obj = cls_list[line]()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        args = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line not in cls_list:
            print("** class doesn't exist **")
        else:
            line.split()
            print(models.storage.all()[]:
                

if __name__ == "__main__":
    HBNBCommand().cmdloop()
