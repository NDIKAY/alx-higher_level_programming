#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a strong to a UTF8 text file.

    Args:
        filename (str): The neme of file to write.
        text (str): The text to write to the file
    Returns:
        The number of characters written.
    """
    with open(filename, "w", enconding="utf-8") as f:
        return f.write(text)
