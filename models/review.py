#!/usr/bin/python3
""" Module for the Review class of tha Air_bnb project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class for the Air_bnb project
    Attributes:
        place_id (str): place being reviewed
        user_id (str): id of user making the reviewed
        text (str): review content
    """

    place_id = ""
    user_id = ""
    text = ""
