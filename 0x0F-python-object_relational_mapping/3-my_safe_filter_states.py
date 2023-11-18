#!/usr/bin/python3

"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    checking the length of the argurment
    """

    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name>".format(
                sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
try:
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
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (state_name,))

    """ Fetch all the rows using fetchall() method """
    data = cursor.fetchall()

    """ Print the result """
    for row in data:
        print(row)
except MySQLdb.Error as e:
    print(f"MySQL Error: {e}")

finally:
    """ Close the cursor """
    cursor.close()

    """ Close the database connection """
    db.close()
