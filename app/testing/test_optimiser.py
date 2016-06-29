#!/usr/bin/env python3

"""
Unittests for optimiser
"""

import unittest
import os
import sys
from optimiser import locationOptimiser

class testGeoCoding(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Read API key from travis environ
        """
        try:
            cls.api_key = os.environ['GMAPS_API_KEY']
        except KeyError:
            print("$GMAPS_API_KEY is undefined")
            print("If running tests locally this must be a valid key")
            sys.exit(1)


    def test_init_bad_key(self):
        """
        Ensure init fails with invalid api_key
        """

        with self.assertRaises(SystemExit):
            locationOptimiser(["a", "b"], "fake")

    def test_init_bad_locs(self):
        """
        Ensure init fails with invalid locs
        """

        with self.assertRaises(SystemExit):
            locationOptimiser([1, "b"], self.api_key)

        with self.assertRaises(SystemExit):
            locationOptimiser("not list", self.api_key)


    def test_correct_init(self):
        """
        Ensure init works with valid key and location
        """

        locs = ['a', 'b']

        with self.assertRaises(SystemExit):
            test = locationOptimiser(locs, self.api_key)

        self.assertEqual(test.origins, collections.Counter(locs))


