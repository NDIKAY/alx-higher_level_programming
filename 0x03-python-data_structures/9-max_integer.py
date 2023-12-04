#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maximum_value = my_list[0]

    for number in my_list:
        if number > maximum_value:
            maximum_value = number
            return maximum_value
