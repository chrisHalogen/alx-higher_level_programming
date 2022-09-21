#!/usr/bin/python3

# print_last_digit: function to write the last digit of a number
# Number: integer input
# last: the final result
# Return: an integer

def print_last_digit(number):
    if number < 0:
        last = (-1 * number) % 10
    else:
        last = number % 10

    print('{}'.format(last), end='')

    return last
