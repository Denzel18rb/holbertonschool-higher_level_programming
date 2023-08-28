#!/usr/bin/python3
"""MySQL State List Module

This module connects to a MySQL database and lists states whose names start with 'N'
from the specified database.

Usage:
    $ python3 state_list.py <username> <password> <database>

"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        cur = conn.cursor()

        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        states = cur.fetchall()

        for state in states:
            print(state)

        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)