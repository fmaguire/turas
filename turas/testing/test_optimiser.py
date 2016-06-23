#!/usr/bin/env python3

"""
Unittests for optimiser
"""

import unittest
from optimiser import locationOptimiser

class testGeoCoding(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        """
        Ensure init fails with invalid api_key
        """

        with self.assertRaises(SystemExit):
            locationOptimiser(["a", "b"], "fake")

        with self.assertRaises(SystemExit):
            locationOptimiser([1, "b"], "fake")

        with self.assertRaises(SystemExit):
            locationOptimiser(["a", "b"], "fake")



