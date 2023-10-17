#!/usr/bin/python3
""" Module for the User class of tha Air_bnb project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class for the Air_bnb project
    Attributes:
        city_id (str): the City id
        user_id (str): the User id
        name (str): Location name
        description (str): Location info
        number_rooms (int): total number of rooms in the place
        number_bathrooms (int): total number of bath rooms in the place
        max_guest (int): maximum guests the place can house
        price_by_night (int): cost of a night's stay at the place
        latitude (float): latitude of a place
        longitude (float): longitude of a place
        amenity_ids (list): contains the Amenity ids(string)
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
