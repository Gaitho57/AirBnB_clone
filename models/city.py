#!/usr/bin/python3
"""
Has a class City that inherits from the BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that manages Cities
    Inherits attributes of the BaseModel Class
    """

    state_id = ""
    name = ""
