#!/usr/bin/python3
class User(BaseModel):
    """
    Class representing a user.

    Attributes:
        email: The user's email address.
        password: The user's password.
        first_name: The user's first name.
        last_name: The user's last name.
    """

    email = CharField(max_length=255)
    password = CharField(max_length=128)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)

    def __repr__(self):
        """String representation of the User object."""
        return (
            f"<User {self.id} ({self.email}) ({self.first_name} {self.last_name})>"
        )
