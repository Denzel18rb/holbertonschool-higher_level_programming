#!/usr/bin/python3
""" Lists all states that matches the argument 4"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Parse command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL server
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object to execute SQL queries
        cur = conn.cursor()

        # Execute the SQL query to select states where name matches the user input
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        # Fetch all rows from the result set
        states = cur.fetchall()

        # Print the results
        for state in states:
            print(state)

        # Close the cursor and connection
        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
