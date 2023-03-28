#!/usr/bin/env python3

""" This will test the person class
"""

import unittest
from classtests import Person

class PersonTest(unittest.TestCase):
    """ Test the person class """
    def setUp(self):
        self.person = Person.Person('Bob', 'Marley', 'Nine Mile, Jamaica',
                                    36, 'Singer',
                                    ['chill', 'funny', 'peaceful'])
    def test_repr(self):
        """ This will be what is printed when you print the object """
        self.assertEqual(repr(self.person), 'Person(Bob, Marley, Nine Mile, Jamaica, 36, Singer, [\'chill\', \'funny\', \'peaceful\'])')


    def test_fullname(self):
        """ Test that the fullname is set """
        self.assertTrue(self.person.fullname, 'Bob Marley')

    def test_email(self):
        """ Creates an email property """
        self.assertEqual(self.person.email, 'Bob.Marley@myprovider.com')

    def test_fullname_setter(self):
        """ Change the fullname using setter """
        self.person.fullname = 'Billy Joel'
        self.assertEqual(self.person.first, 'Billy')
        self.assertEqual(self.person.last, 'Joel')

    @unittest.expectedFailure
    def test_fullname_deleter(self):
        """ test the deleter and assert name isn't bob anymore """
        del self.person.fullname
        self.assertEqual(self.person.first, 'Bob')
        self.assertEqual(self.person.first, 'Billy')
        
    def test_should_eat_icecream(self):
        self.assertTrue(self.person.should_eat_icecream())
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
