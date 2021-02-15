#!/usr/bin/python3

""" FileStorage class that serializes and deserializes JSON file """

import json
from models.base_model import BaseModel 
from models.user import User 
from models.place import Place 
from models.state import State 
from models.city import City 
from models.amenity import Amenity 
from models.review import Review 

class FileStorage:
    """ Define FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary __objects """
        return self.__objects

    def new(self,obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serialize object to json file """
        jsobj = {}
        for key in self.__objects.keys():
            jsobj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(jsobj, file)

    def reload(self):
                """ Deselialize a Json file to __object """
                try:
                    obj = {}
                    with open(__file_path, 'r') as file:
                        obj = json.load(__file_path)
                    for key, value in obj.item():
                                vals = eval(value ['__class__'])(**value)
                                self.__objects[key] = vals
                except:
                    pass
