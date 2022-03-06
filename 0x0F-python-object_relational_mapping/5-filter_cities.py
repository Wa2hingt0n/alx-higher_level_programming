#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa by id, city and state
    Usage: <script_name> <username> <password> <database_name>
"""
import MySQLdb
import sys


if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = conn.cursor()
    query = """SELECT name FROM cities
    WHERE state_id = (SELECT id FROM states WHERE name = %s)
    ORDER BY id ASC"""
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()

    query_list = []
    for row in query_rows:
        query_list.append(row[0])
    state_str = ", ".join(query_list)
    print(state_str)

    cur.close()
    conn.close()
