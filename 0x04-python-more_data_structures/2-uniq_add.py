#!/usr/bin/python3
# 2-uniq_add.py


def uniq_add(my_list=[]):
    """
    Add all unique integers in a list (once for each integer).
    """
    output = 0
    for item in set(my_list):
        output += item
    return (output)
