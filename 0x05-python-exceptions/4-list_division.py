#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divide two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of the resulting list.

    Returns:
        list: A new list with all divisions.
    """
    result_list = []

    for i in range(list_length):
        try:
            a = my_list_1[i] if i < len(my_list_1) else 0
            b = my_list_2[i] if i < len(my_list_2) else 0

            if not (isinstance(a, (int, float))
                    and isinstance(b, (int, float))):
                print("wrong type")
                result_list.append(0)
            elif b == 0:
                print("division by 0")
                result_list.append(0)
            else:
                result = a / b
                result_list.append(result)
        except IndexError:
            print("out of range")
            result_list.append(0)

    return result_list
