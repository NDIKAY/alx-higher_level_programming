#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_mine =()
    if len(sentence) == 0:
        tuple_mine = 0, None
    else:
        tuple_mine = len(sentence), sentence[0]
    return tuple_mine
