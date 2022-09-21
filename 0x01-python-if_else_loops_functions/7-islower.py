#!/usr/bin/python3
# islower - function to test if input is lower case
# Return - True or False
def islower(char):
    if (ord(char) > 96 and ord(char) < 123):
        return True
    else:
        False
