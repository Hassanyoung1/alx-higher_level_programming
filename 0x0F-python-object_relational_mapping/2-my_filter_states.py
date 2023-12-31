#!/usr/bin/python3

"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb
from sys import argv

if __name__ == "__main__":

    """checking the length of the argurment"""

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

    """ Execute the SQL query """

    query = """SELECT * FROM states WHERE `name` = '{}'
                   ORDER BY `id`"""
    cursor.execute(query.format(argv[4]))

    """ Fetch all the rows using fetchall() method """

    data = cursor.fetchall()

    """ Print the result """

    for row in data:
        if row[1] == argv[4]:
            print(row)

    """ Close the cursor """

    cursor.close()

    """ Close the database connection """

    db.close()
