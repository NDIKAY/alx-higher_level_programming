#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maximum_value = my_list[0]

    for i in range(1, my_list[len(my_list)] - 1):
        if my_list[i] > maximum_value:
            maximum_value = my_list[i]
    return max_value 
