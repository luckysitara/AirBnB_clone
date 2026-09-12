#!/usr/bin/python3
""" Module for the User class of the AirBnB project """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class for the AirBnB project
    Attributes:
        email (str): user's email address
        password (str): user's password
        first_name (str): user's first name
        last_name (str): user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
