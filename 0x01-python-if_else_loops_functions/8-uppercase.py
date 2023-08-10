#!/usr/bin/python3

def uppercase(str):

    rslt = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            rslt += chr(ord(char) - ord('a') + ord('A'))
        else:
            rslt += char
    print("{}".format(rslt))
