#!/usr/bin/env python3

'''Defines the BaseModel class.'''
from models.base_model import BaseModel
import json
import os


class FileStorage:
    '''
    serializes instances to a JSON file and deserializes back to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        returns the dictionary
        '''
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''
        Serialize __objects to the JSON file __file_path.
        '''
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists).
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    class_name, obj_id = key.split(".")
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
