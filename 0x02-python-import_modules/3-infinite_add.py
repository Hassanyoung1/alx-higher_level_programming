#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    arg_num = len(argv)
    sum = 0
    for num in range(1, arg_num):
        sum += int(argv[num])
    print(sum)
