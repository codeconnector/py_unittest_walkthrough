#!/usr/bin/env python3
""" Core routines for funprog """

from funprog import utils


def return_a_sentence_from_number(number):
    """ Returns a sentence given a number as an integer
    Args:
        number (int): the number to use
    Returns:
        sentence (str): the sentence with number
    """
    new_num = utils.number_plus_four(number)
    str_num = utils.convert_number_to_str(new_num)
    sentence = utils.insert_into_sentence(str_num)
    return sentence
