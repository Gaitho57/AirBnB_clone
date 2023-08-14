#!/usr/bin/python3
#!/usr/bin/python3
"""
Module for the class User that inherits from the BaseModel class
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    A User class that inherits from the BaseModel class.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize User object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
