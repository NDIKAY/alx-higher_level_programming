#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student """

    def __init__(self, first_name, last_name, age):
        """Initiate a new student.

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of a student
            age (int): the age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=none):
        """Get a dictionnary representation of student.

        if attrs is a list of string, represents only those attributes included in the list

        Args:
            attrs (list): The attributes to represent
        """
        if (type(attrs) == list and 
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs in hasttr(self, k)}
        return self.__dict__

