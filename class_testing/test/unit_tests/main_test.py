#!/usr/bin/env python3

""" This is going to execute the main function
"""

import os
import unittest

class MainTest(unittest.TestCase):
    """ Test the main entry point of the program """
    def setUp(self):
        pass

    def test_main(self):
        """ Should return 0 because of success """
        result = os.system("classtests")
        self.assertEqual(result, 0)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
