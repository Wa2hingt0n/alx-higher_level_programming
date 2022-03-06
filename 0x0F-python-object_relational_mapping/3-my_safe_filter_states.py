#!/usr/bin/python3
""" Takes an argument and displays all values in the `states` table of the
    hbtn_0e_0_usa database where `name` matches the argument.

    Usage: <3-my_safe_filter_states> <username> <password> <database> <name>
"""
import sys
import MySQLdb


if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE states.name=\"{}\" ORDER BY states.id"
        .format(sys.argv[4]))

    query_row = cur.fetchall()
    for row in query_row:
        if row[1] == sys.argv[4]:
            print(row)

    cur.close()
    conn.close()
