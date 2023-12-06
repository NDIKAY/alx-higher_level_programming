#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueIntengers =set()
    for num in my_list:
        uniqueIntengers.add(num)
    result = sum(uniqueIntengers)
    return result
        

