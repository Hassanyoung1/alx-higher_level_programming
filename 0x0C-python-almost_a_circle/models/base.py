#!/usr/bin/python3

"""This module defines the Base class."""


import json
from os.path import exists
import csv

""" Declare Class """


class Base:
    """
    The Base class for managing object IDs.

    Attributes:
        __nb_objects (int): A class attribute to
        keep track of the number of objects created.

    Methods:
        __init__(self, id=None): Initializes a
        new instance of the Base class.
        to_json_string(list_dictionaries): Converts
        a list of dictionaries to a JSON string.
        save_to_file(cls, list_objs): Saves a
        list of objects to a JSON file.
        from_json_string(json_string): Converts a
        JSON string to a list of dictionaries.
        create(cls, **dictionary): Creates a new
        instance of the class with attributes from a dictionary.
        load_from_file(cls): Loads a list of objects from a JSON file.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class.

        Args:
            id (int): An optional ID to set for the object.
                If not provided, a unique ID will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of
            dictionaries to be converted.

        Returns:
            str: A JSON string representing the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            cls (class): The class to which the objects belong.
            list_objs (list): A list of objects to
            be saved to a JSON file.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write('[]')
            else:
                empty_list = []
                for each_inst in list_objs:
                    empty_list.append(each_inst.to_dictionary())
                file.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string to be converted.

        Returns:
            list: A list of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class with attributes from a dictionary.

        Args:
            cls (class): The class for which to create a new instance.
            **dictionary: Keyword arguments representing attributes.

        Returns:
            cls: A new instance of the class with the specified attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of objects from a JSON file.

        Args:
            cls (class): The class from which to load objects.

        Returns:
            list: A list of objects loaded from the JSON file.
        """
        file_name = cls.__name__ + ".json"
        if exists(file_name) is False:
            return []
        else:
            with open(file_name, 'r', encoding="utf-8") as file:
                read_file = file.read()
                loads = cls.from_json_string(read_file)
                instance = [cls.create(**items) for items in loads]
            return instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize objects to a CSV file.

        Args:
            cls (class): The class itself.
            list_objs (list): A list of objects to be serialized.

        Returns:
            None
        """
        file_name = cls.__name__ + ".csv"

        with open(file_name, 'w', newline='') as csv_file:
            dict_objs = [each_obj.to_dictionary() for each_obj in list_objs]

            # Extract fieldnames from the first object's dictionary
            if dict_objs:
                fieldnames = list(dict_objs[0].keys())
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                for each_dict in dict_objs:
                    writer.writerow(each_dict)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize objects from a CSV file.

        Returns:
            list: A list of object instances created from the CSV data.
        """
        file_name = cls.__name__ + ".csv"
        instance_list = []

        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']

                instance = {field: int(row[field]) for field in fields}
                instance_list.append(instance)

        return [cls.create(**each_dict) for each_dict in instance_list]
