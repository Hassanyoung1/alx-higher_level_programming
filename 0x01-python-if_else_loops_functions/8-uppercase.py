#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()
