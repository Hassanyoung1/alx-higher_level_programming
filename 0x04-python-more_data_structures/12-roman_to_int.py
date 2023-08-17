#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int_mapping = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = roman_to_int_mapping[roman_string[0]]

    for i in range(1, len(roman_string)):
        value = roman_to_int_mapping[roman_string[i]]
        prev_value = roman_to_int_mapping[roman_string[i - 1]]

        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value

    return total
