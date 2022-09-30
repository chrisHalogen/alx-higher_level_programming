#!/usr/bin/python3
# 102-complex_delete.py
# Boluwaji Oladimeji


def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for item, item_value in a_dictionary.items():
            if item_value == value:
                del a_dictionary[item]
                break

    return (a_dictionary)
