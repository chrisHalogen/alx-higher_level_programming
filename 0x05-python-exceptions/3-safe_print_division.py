#!/usr/bin/python3


def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        output = a / b
    except (TypeError, ZeroDivisionError):
        output = None
    finally:
        print("Inside result: {}".format(output))
    return (output)
