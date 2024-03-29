#!/usr/bin/python3
""" A script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument """
import MySQLdb
import sys


if __name__ == "__main__":
    db_connect = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)
    cursor = db_connect.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'"
        .format(sys.argv[4]))
    rows = cursor.fetchall()
    for single_row in rows:
        print(single_row)
    cursor.close()
    db_connect.close()
