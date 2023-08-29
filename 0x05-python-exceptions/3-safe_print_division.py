#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divide two integers and print the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float or None: The value of the division, or None if an exception
    """
    div_result = None
    try:
        div_result = a/b
    except ZeroDivisionErrror:

        pass
    finally:
        print("Inside result: {}".format(div_result))
        return div_result
