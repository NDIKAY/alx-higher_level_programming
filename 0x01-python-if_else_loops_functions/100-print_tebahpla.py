#!/usr/bin/python3
alphabet ='abcdefghijklmnopqrstuvwxyz'
reversed_alphabet = alphabet[::-1]
for i in range(len(reversed_alphabet)):
    char = reversed_alphabet[i]
    if i % 2 == 0:
        char = char.upper()
    print("{}".format(char), end="")
    
