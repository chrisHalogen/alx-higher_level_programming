#!/usr/bin/python3
"""6. Find a peak"""


def find_peak(list_of_integers):
    """ a function that finds a peak in a list of unsorted integers. """
    if list_of_integers == []:
        return None

    count = len(list_of_integers)
    half = int(count / 2)
    arr = list_of_integers

    if half - 1 < 0 and half + 1 >= count:
        return arr[half]
    elif half - 1 < 0:
        return arr[half] if arr[half] > arr[half + 1] else arr[half + 1]
    elif half + 1 >= count:
        return arr[half] if arr[half] > arr[half - 1] else arr[half - 1]

    if arr[half - 1] < arr[half] > arr[half + 1]:
        return arr[half]

    if arr[half + 1] > arr[half - 1]:
        return find_peak(arr[half:])
    return find_peak(arr[:half])
