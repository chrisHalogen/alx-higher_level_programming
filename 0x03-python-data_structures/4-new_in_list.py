#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    """
    Replace an element in a duplicated list at a position.
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    duplicate = [item for item in my_list]
    duplicate[idx] = element
    return (duplicate)
