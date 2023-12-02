#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            return (none)
        elif idx > len(my_list):
            return none
        elif i == idx:
            return (idx)
