#!/usr/bin/python3
'''
    class User that inherits from BaseModel

    '''
from models.base_model import BaseModel


class City(BaseModel):
    '''
        defining city class
    '''
    state_id = ""
    name = ""
