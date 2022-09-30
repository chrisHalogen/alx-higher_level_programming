#!/usr/bin/python3
# 100-weight_average.py


def weight_average(my_list=[]):
    if not my_list:
        return 0

    score = 0
    weight = 0
    for a, b in my_list:
        score += (a * b)
        weight += b
    return (score / weight)
