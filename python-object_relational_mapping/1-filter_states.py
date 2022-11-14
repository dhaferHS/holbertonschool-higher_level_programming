#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],

    )
    thecursor = db.cursor()
    thecursor.execute("SELECT name FROM states WHERE name LIKE BINARY 'n%' ORDER BY id ASC")
    rows = thecursor.fetchall()
    for row in rows:
        print(row)
    thecursor.close()
    db.close()
