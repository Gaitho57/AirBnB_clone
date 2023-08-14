#!/usr/bin/python3
"""
Has a class Review that has the BaseModel class as parent
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Organizes attributes of the class Review
    Inherits attributes of the BaseModel Class
    """

    place_id = ""
    user_id = ""
    text = ""
