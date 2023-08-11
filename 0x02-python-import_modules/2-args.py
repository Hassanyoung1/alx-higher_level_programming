#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    number_of_argv = len(argv)

    if number_of_argv == 1:
        print(number_of_argv - 1, "arguments.")

    elif number_of_argv == 2:
        print(number_of_argv - 1, "argument:")
        print("{}: {}".format(number_of_argv - 1, argv[1]))
    elif number_of_argv > 2:
        print(number_of_argv - 1, "arguments:")

        for num in range(1, number_of_argv):
            print("{}: {}".format(num, argv[num]))
