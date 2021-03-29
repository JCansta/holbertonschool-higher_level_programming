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
    cur.execute("SELECT cities.name FROM cities\
    INNER JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (name, ))
    rows = cur.fetchall()
    count = 0
    for row in rows:
        print(list(row)[0], end="")
        if (count == len(rows) - 1):
            print()
        else:
            print(", ", end="")
        count += 1
    cur.close()
    db.close()
