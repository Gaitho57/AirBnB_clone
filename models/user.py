#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):

    """
    Class representing a User.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a User instance.
        """
        super().__init__(*args, **
