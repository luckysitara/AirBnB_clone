#!/usr/bin/python3
""" Module for the City class of tha Air_bnb project """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class for the Air_bnb project
    Attributes:
        state_id(str): states's id
        name (str): city's firstname
    """

    state_id = ""
    name = ""
