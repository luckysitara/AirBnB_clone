#!/usr/bin/python3
""" Module for the User class of tha Air_bnb project """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class for the Air_bnb project
    Attributes:
        email (str): user's email address
        password (str): user's password
        first_name (str): user's firstname
        last_name (str): user's last_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
