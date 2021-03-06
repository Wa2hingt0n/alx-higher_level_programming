#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa that start with letter N
    in ascending order
    Usage : <1_filter_states.py> <username> <user_password> <hbtn_0e_0_usa>
"""


import MySQLdb
import sys


if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == "N":
            print(row)

    cur.close()
    conn.close()
