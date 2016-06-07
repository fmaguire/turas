#!/usr/bin/env python3

import sys
import collections
import googlemaps

def optimise_location(starting_places, api_key=False):
    """
    Function to optimise the location for minimal distance of a
    range of locations
    """
    gmaps = googlemaps.Client(key=api_key)

    origins = parse_inputs(filename=starting_places)

    geocoded_origins = geocode_addresses(origins, gmaps)

    print(geocoded_origins)


def geocode_addresses(origins, gmaps):
    """
    Take in a counter and geocode the addresses
    """
    coded_origins = []

    for k,v in origins.items():
        coded_origins.append((get_loc_from_address(k, gmaps), v))

    return coded_origins


def parse_inputs(filename=False):
    """
    Parse input set of locations and return a tallied
    count of the locations
    """
    if filename:
        with open(filename, 'r') as fh:
            locations = [x.strip() for x in fh.readlines()]

    tallied_locations = collections.Counter(locations)

    return tallied_locations


def get_loc_from_address(address_string, gmaps):
    """
    Get geocoded address from text address
    """
    geocode_result = gmaps.geocode(address_string)
    if len(geocode_result) == 0:
        print("Address not found: {}".format(address_string))
        assert False
    else:
        loc = geocode_result[0]['geometry']['location']
        loc = (loc['lat'], loc['lng'])

    return loc


def get_address_from_loc(geocode, gmaps):
    """
    Get text address from geocode
    """
    address = gmaps.reverse_geocode(geocode)
    return address

def find_midpoint(geocodes, gmaps):
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

if __name__=='__main__':

    api_key = sys.argv[2]
    starting_places = sys.argv[1]
    optimise_location(starting_places, api_key)

