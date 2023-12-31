#!/usr/bin/python3

"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb
from sys import argv

if __name__ == "__main__":

    """ Checking the length of the argument """

    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name>".format(
                sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]

    """ Connect to MySQL database """

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    """ Create a cursor object using cursor() method """

    cursor = db.cursor()

    """  Execute the SQL query """

    query = "SELECT cities.id, cities.name, states.name " \
            "FROM cities INNER JOIN states ON cities.state_id=states.id " \
            "WHERE states.name = %s " \
            "ORDER BY cities.id"

    cursor.execute(query, (argv[4],))

    """ Fetch all the rows using fetchall() method"""
    data = cursor.fetchall()

    """  Print the result """
    city_string = ", ".join(row[1] for row in data)
    print(city_string)
    """ Close the cursor """
    cursor.close()

    """ Close the database connection """
    db.close()
