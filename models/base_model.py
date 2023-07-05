#!/usr/bin/env python3
'''Defines the BaseModel class.'''

from datetime import datetime
import uuid
import json
import models


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """
        return in ISO format
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self, *args, **kwargs):
        """Updates the updated_at attribute
        with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()


    def to_dict(self):
        '''
        make a dictionary for the logs
        '''
        dictionary = self.__dict__
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
