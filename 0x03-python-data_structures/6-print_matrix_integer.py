#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for element in row:
                print("{:d}".format(element), end=" " 
                    if element != row[-1] else "")
            print()
