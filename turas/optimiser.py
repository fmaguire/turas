#!/usr/bin/env python3

import numpy as np
import sys
import collections
import googlemaps

class locationOptimiser:
    """
    Class to optimise the location for minimal distance of a
    range of locations and a gmaps API key
    """

    def __init__(self, name, origins_list, api_key):
        """
        Check input starting places and api
        """
        try:
            self.gmaps = googlemaps.Client(key=api_key)
        except ValueError:
            print("API key provided is invalid")
            sys.exit(1)

        if type(origins_list) is not list:
            print("List of origins must be provided")
            sys.exit(1)

        if not all([type(x) == str for x in origins_list]):
            print("Origins must be provided as strings in list")
            sys.exit(1)

        self.name = name

        self.origins = collections.Counter(origins_list)


    def get_best_location(self):
        """
        Find best conference location
        """
        geocoded_origins = self.geocode_addresses(self.origins)

        midpoint = self.find_midpoint(geocoded_origins)

        print(midpoint)

        candidate_locs = self.get_candidates(midpoint)

        return candidate_locs


    def geocode_addresses(self, origins):
        """
        Take in a counter and geocode the addresses
        """
        coded_origins = []

        for k,v in origins.items():
            coded_origins.append((self.get_loc_from_address(k), v))

        return coded_origins


    def get_loc_from_address(self, address_string):
        """
        Get geocoded address from text address
        """
        geocode_result = self.gmaps.geocode(address_string)
        if len(geocode_result) == 0:
            print("Address not found: {}".format(address_string))
            assert False
        else:
            loc = geocode_result[0]['geometry']['location']
            loc = (loc['lat'], loc['lng'])

        return loc

    def find_midpoint(self, geocodes):
        """
        Find geocode of midpoint of a list of geocodes
        """

        # unroll geocode list
        # i.e. change from counter to full redundancy
        unrolled_codes = []
        for loc in geocodes:
            for num in range(loc[1]):
                unrolled_codes.append(loc[0])

        print(unrolled_codes)

        xyz = np.array([0., 0., 0.])

        for lat, lon in unrolled_codes:
            xyz[0] += np.cos(lat) * np.cos(lon)
            xyz[1] += np.cos(lat) * np.sin(lon)
            xyz[2] += np.sin(lat)

        xyz = xyz / len(unrolled_codes)

        center = (np.arctan2(xyz[2],
                             np.sqrt(xyz[0] * xyz[0] + xyz[1] * xyz[1])),
                  np.arctan2(xyz[1], xyz[0]))

        return center


    def get_candidates(self, midpoint):
        """
        Get candidate locations closest to weighted midpoint
        """

        geocoded_candidates = self.nearest_cities(midpoint)

        candidates = [(self.get_address_from_loc(x[0]),
                       x[1]) for x in geocoded_candidates]

        return candidates


    def nearest_cities(self, geocode):
        """
        Return list of tuple with nearest cities with airpoints to geocode
        and their distance from geocode
        """
        self.gmaps()
        pass


    def get_address_from_loc(self, geocode):
        """
        Get text address from geocode
        """
        address = self.gmaps.reverse_geocode(geocode)
        return address


if __name__=='__main__':

    api_key = sys.argv[2]
    starting_places = sys.argv[1]
    locationOptimiser("test", starting_places, api_key)

