#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight_sum = sum(score * weight for score, weight in my_list)
    weightInTotal = sum(weight for _, weight in my_list)
    averageWeight = weight_sum / weightInTotal
    return averageWeight
