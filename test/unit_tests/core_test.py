#!/usr/bin/env python3

import unittest
import funprog.core as core

class Core(unittest.TestCase):
    def setUp(self):
        """ This is where you define any inputs to code """
        self.number = 4

    def test_return_a_sentence_from_number(self):
        self.assertEqual(core.return_a_sentence_from_number(self.number), "The shepherd had 8 sheep")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
