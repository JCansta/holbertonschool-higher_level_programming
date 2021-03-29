#!/usr/bin/python3
"""
    print database with filters
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    name = argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
    WHERE name LIKE '{}'".format(name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
