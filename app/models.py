#!/usr/bin/env python3

from turas import gmaps
import numpy as np

"""
# Replace the API key below with a valid API key.
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Geocoding and address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

"""

def get_loc_from_address(address_string):
    """
    Get geocoded address from text address
    """

    geocode_result = gmaps.geocode(address_string)
    return geocode_result


def get_address_from_loc(geocode):
    """
    Get text address from geocode
    """
    address = gmaps.reverse_geocode(geocode)
    return address

def find_midpoint(geocodes):
    """
    Find geocode of midpoint of a list of geocodes
    """

    xyz = np.array([0., 0., 0.])

    for lat, lon in geocodes:
        xyz[0] += np.cos(lat) * np.cos(lon)
        xyz[1] += np.cos(lat) * np.sin(lon)
        xyz[2] += np.sin(lat)

    xyz = xyz / len(geocodes)

    center = (np.arctan2(xyz[2],
                         np.sqrt(xyz[0] * xyz[0] + xyz[1] * xyz[1])),
              np.arctan2(xyz[1], xyz[0]))

    return center


