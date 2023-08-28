#!/usr/bin/python3
""" Lists all states that matches the argument 4"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
<<<<<<< HEAD
            )
        cur = conn.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
=======
        )
        cur = conn.cursor()
        query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
>>>>>>> aacb4d93a2c3db63b9dff5b414be9bc117a2d32d
        cur.execute(query, (state_name,))
        states = cur.fetchall()
        for state in states:
            print(state)
        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
