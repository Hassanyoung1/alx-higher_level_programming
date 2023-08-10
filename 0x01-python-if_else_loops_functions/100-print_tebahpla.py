#!/usr/bin/python3

for c in range(90, 64, -1):
    char = chr(c)
    if c % 2 == 0:
        char = char.lower()
    print("{}".format(char), end="")
