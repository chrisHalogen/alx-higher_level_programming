#!/usr/bin/python3
""" Python ORM Exercise """
import MySQLdb
import sys


if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db_connect.cursor()
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN states
                   ON states.id=cities.state_id WHERE 
                   states.name=%s""", (sys.argv[4],))
    rows = cursor.fetchall()
    output_str_list = list(single_row[0] for single_row in rows)
    print(*output_str_list, sep=", ")
    cursor.close()
    db_connect.close()