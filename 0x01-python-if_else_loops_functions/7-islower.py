#!/usr/bin/python3

def islower(c):
    lower = ord(c)
    for num in range(97, 123):
        if lower == num:
            return True
    return False
