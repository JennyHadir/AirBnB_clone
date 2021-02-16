#!/usr/bin/python3
""" The entry point of the command interpreter """

import shlex
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

    def precmd(self, line):
        """Hook method executed just before the command line is interpreted
        """
        cmnd, args, line = self.parseline(line)
        if cmnd in cls_list:
            cls_name = cmnd
            cmnd = args[1: args.find('(')]
            args = args[args.find('(') + 1:-1]
            args = args.replace(',', '')
            line = ' '.join([cmnd, cls_name, args])
        return line

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
        """ prints the string representation of an instance
        """
        args = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in cls_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            print("searching for: {}".format(args[0] + '.' + args[1]))
            try:
                print(models.storage.all()[args[0] + '.' + args[1]])
            except:
                print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances
        """
        args = shlex.split(line)
        obj_list = []
        if len(line) == 0:
            for obj in models.storage.all().values():
                obj_list.append(obj.__str__())
            print(obj_list)
        else:
            if args[0] not in cls_list:
                print("** class doesn't exist **")
            else:
                for obj in models.storage.all().values():
                    if type(obj).__name__ == args[0]:
                        obj_list.append(obj.__str__())
                print(obj_list)

    def do_update(self, line):
        """ Updates an instance based on the class name and id
        """
        args = shlex.split(line)
        objs_dict = models.storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in cls_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            inst_name = args[0] + '.' + args[1]
            if inst_name not in objs_dict:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = objs_dict[inst_name]
                casted_value = type(getattr(obj, args[2]))(args[3])
                setattr(obj, args[2], casted_value)
                obj.save()

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = shlex.split(line)
        objs_dict = models.storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in cls_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            inst_name = args[0] + '.' + args[1]
            if inst_name not in objs_dict:
                print("** no instance found **")
            else:
                del objs_dict[inst_name]
                models.storage.save()

    def do_count(self, line):
        """Retrieve the number of instances of a class
        """
        count = 0
        for k in models.storage.all().keys():
            if line in k:
                count += 1
        print(count)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
