#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    output = list(a_dictionary.keys())[0]
    max_value = a_dictionary[output]
    for item, item_value in a_dictionary.items():
        if item_value > max_value:
            max_value = item_value
            output = item
    return (output)
