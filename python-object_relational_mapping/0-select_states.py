#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa."""


import MySQLdb
from sys import argv

if __name__ == "__main":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        username=argv[1],
        password=argv[2],
        database=argv[3],
    )

    thecursor = db.cursor()

    thecursor.execute("SELECT id, name FROM states ORDED BY id")

    therows = thecursor.fetchall()

    for row in therows:
        print(row)

    thecursor.close()
    db.close()
