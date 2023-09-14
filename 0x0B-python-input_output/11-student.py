#!/usr/bin/python3

"""Defines a class Student."""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student object.

        Args:
            attrs (list, optional): A list of attribute names
            to include in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            return student_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.

        Args:
            json (dict): A dictionary containing attribute
            names and their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
