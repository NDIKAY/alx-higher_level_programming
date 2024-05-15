#!/usr/bin/python3
"""Defines text file-reading function"""


def read_file(filename=""):
    """print the contents of a UTF8 text file to stdout."""
    with open(filename, encording="utf-8") as f:
        print(f.read(), end="")
