#!/usr/bin/python3
""" Lists all states that matches the argument 4"""
import MySQLdb
import sys

def list_cities_by_state(username, password, database_name, state_name):
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

        cursor = db.cursor()

        query = "SELECT cities.id, cities.name FROM cities " \
                "JOIN states ON cities.state_id = states.id " \
                "WHERE states.name = %s " \
                "ORDER BY cities.id ASC"

        cursor.execute(query, (state_name,))

        cities = cursor.fetchall()
        for city in cities:
            print(city)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_cities_by_state(username, password, database_name, state_name)
