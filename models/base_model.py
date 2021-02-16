#!/usr/bin/python3
""" Define a BaseModel class """

import uuid
import datetime
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """ BaseModel class """
    def __init__(self, *args, **kwargs):
        """ Initialization """
        if kwargs:
            for key, value in kwargs.items():
                if __name__ != "__class__":
                    setattr(self, key, value)
                if key == 'update_at' or key == 'created_at':
                    self.__dict__[key] = datetime.strptime(value, time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String representation of BaseModel """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__
                                     )

    def save(self):
        """ Update the update_at with the current datetime """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key/values """
        dict = self.__dict__.copy()
        dict["created_at"] = dict["created_at"].strftime(time_format)
        dict["updated_at"] = dict["updated_at"].strftime(time_format)
        dict["__class__"] = self.__class__.__name__
        return dict
