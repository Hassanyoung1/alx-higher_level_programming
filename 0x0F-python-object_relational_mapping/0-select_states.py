#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Connect to MySQL database """
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    """ Create a cursor object using cursor() method """
    cursor = db.cursor()

    """ Execute the SQL query """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """ Fetch all the rows using fetchall() method """
    data = cursor.fetchall()

    """ Print the result """
    for row in data:
        print(row)
    """ Close the cursor """
    cursor.close()

    """ Close the database connection """
    db.close()
