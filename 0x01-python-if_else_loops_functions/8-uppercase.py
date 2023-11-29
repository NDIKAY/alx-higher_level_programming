#!/usr/bin/python3
def uppercase(str):
    input_str =""

    for char in str:
        if 'a' <= char <= 'z':
            input_str += "{}".format(chr(ord(char) - ord('a') + ord('A')))
        else:
            input_str += "{}".format(char)
    print(input_str, end="")
    print()

