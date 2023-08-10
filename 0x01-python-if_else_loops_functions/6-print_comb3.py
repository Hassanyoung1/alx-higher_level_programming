#!/usr/bin/python3

for tens in range(10):
    for ones in range(tens + 1, 10):
        if tens != 0 or ones != 0:
            if tens == 8 and ones == 9:
                break
            else:
                print("{:02}, ".format(tens * 10 + ones), end="")
print("{:02}".format(89))
