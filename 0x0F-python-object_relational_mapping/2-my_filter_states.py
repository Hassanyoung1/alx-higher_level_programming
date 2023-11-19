#!/usr/bin/python3

""" takes an argument and displays all values from database hbtn_0e_0_usa."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cursor = db.cursor()
    query = """SELECT * FROM states WHERE `name` = '{}'
                   ORDER BY `id`"""
    cursor.execute(query.format(argv[4]))
    states = cursor.fetchall()

    for state in states:
        if state[1] == argv[4]:
            print(state)

    cursor.close()
    db.close()
