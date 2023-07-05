#!/usr/bin/env python3
'''Defines the BaseModel class.'''

from datetime import datetime
from uuid import uuid4


class BaseModel:
    '''
    Defines the BaseModel class.
    '''
    def __init__(self, *args, **kwargs):
        """
           Initialization of the base model

        """
        self.id = str(uuid4)
        self.created_at = self.updated_at = datetime.utcnow
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key =="updated_at":
                    value == datetime.strftime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
