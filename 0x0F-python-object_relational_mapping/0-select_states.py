#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db_connect.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for single_row in rows:
        print(single_row)
    cursor.close()
    db_connect.close()