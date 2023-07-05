#!/usr/bin/env python3

'''Defines the BaseModel class.'''
from models.base_model import BaseModel
import json


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
        '''
        adds the object
        '''
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

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
        reloads the object
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                new_dict = json.load(file)
                for obj, value in new_dict.items():
                    class_name, obj_id = obj.split(".")
                    obj_instance = eval(class_name)(**value)
                    self.__objects[obj] = obj_instance
        except FileNotFoundError:
            pass
