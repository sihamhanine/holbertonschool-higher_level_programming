#!/usr/bin/python3
"""
Defines modules 5-filter_cities takes in an argument
and displays lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to database and get the cities
    from database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id \
                WHERE states.name LIKE BINARY %s \
                ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()

    # Extract city names from the results
    city_names = []
    for row in rows:
        city_names.append(row[0])
    
    # Print the city names joined by commas
    print(", ".join(city_names))

    cur.close()
    db.close()
