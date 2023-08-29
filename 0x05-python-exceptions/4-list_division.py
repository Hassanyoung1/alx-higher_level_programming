#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]

            try:
                division = a / b
            except ZeroDivisionError:
                print("division by 0")
                division = 0
            except TypeError:
                print("wrong type")
                division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list.append(division)

    return new_list
