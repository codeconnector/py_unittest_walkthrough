#!/usr/bin/env python3

""" This is a module to test out some class based python functionality
We will:
  1. Create a class called Person
  2. We will give that person attributes
  3. We will have methods that change some attributes
  4. We will test
"""

class Person:
    """ A person with some characteristics
        Args:
            first (str): First Name
            last (str): Last Name
            address (str): home address
            age (int): age
            occupation (str): job
            character_traits (list): 3 things about them
    """
    def __init__(self, first, last, address, age, occupation=None, character_traits=None):
        self.first = first
        self.last = last
        self.address = address
        self.age = age
        self.occupation = occupation
        self.character_traits = character_traits

    def __repr__(self):
        return f'Person({self.first}, {self.last}, {self.address}, {self.age}, {self.occupation}, {self.character_traits})'
    
    @property
    def fullname(self):
        """ full name of person """
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        """ email of person """
        return '{}.{}@myprovider.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        """ Set the first and last name given a fullname """
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        """ Deleting a person's full name """
        self.first = None
        self.last = None

    @staticmethod
    def should_eat_icecream():
        return True
