#!/usr/bin/env python3

from funprog import utils, core

def main():
    """ Main Routine """
    args = utils.get_args()
    
    sentence = core.return_a_sentence_from_number(args.number_to_add)
    print(sentence)

if __name__ == "__main__":
    main()
