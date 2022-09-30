#!/usr/bin/python3
# 1-search_replace.py


def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element by another in a new list.
    """
    output = my_list[:]
    for item in range(len(output)):
        if output[item] == search:
            output[item] = replace
    return (output)
