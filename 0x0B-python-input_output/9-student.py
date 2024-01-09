#!/usr/bin/python3
"""Defines aa class student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student,

        Args:
            first_name (str): The first name of the student.
            last name (str): the last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = Last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of student"""
        return self.__dict__