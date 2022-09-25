#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    even_numbers = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            even_numbers.append(True)
        else:
            even_numbers.append(False)

    return (even_numbers)
