#!/usr/bin/env python3

'''Defines the BaseModel class.'''
from models.base_model import BaseModel
import json
import os
import uuid


class FileStorage:
    '''serializes instances to a JSON file and deserializes back to instances'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        returns the dictionary
        '''
        return self.__objects

    def new(self, obj):
        '''
        adds the object
        '''
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        '''
        saves the dictionary
        '''
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        reloads the object
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    class_name, obj_id = key.split(".")
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
