#!/usr/bin/env python3
"""
This is a fun utility script for testing
"""

import argparse

from funprog import __version__

def get_args():
    """ Get args
    Args: None
    Returns:
        args (Namespace): Argparse object
    """

    parser = argparse.ArgumentParser(prog="funprog", description="Command line arguments")
    parser.add_argument("-v", "--version", action="version", version="funprog %s"%(__version__))
    parser.add_argument("-n", "--number_to_add", type=int, required=True,
                        help="The number to add.")
    args = parser.parse_args()
    return args

def number_plus_four(number):
    """ Adds a number to 4
    Args:
        number (int): the number to add to 4
    Returns:
        number + 4 (int): the number with 4 added to it
    """
    return number + 4

def convert_number_to_str(number):
    """ Converts a number to a string
    Args:
        number (int): number being converted to string
    Returns:
        number (str): the number as a string
    """
    return str(number)

def insert_into_sentence(number):
    """ Inserts a number into the sentence
    Args:
        number (int | str): number to be added to string
    Returns:
        sentence (str): sentence to return
    """
    try:
        assert isinstance(number, str)
    except:
        number = str(number)
    return "The shepherd had %s sheep" %number

                        
