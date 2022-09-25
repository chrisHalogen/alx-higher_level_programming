#!/usr/bin/python3
def no_c(my_string):
    output = []
    [output.append(item) for item in my_string if item != 'c' and item != 'C']
    output = ''.join(output)
    return output
