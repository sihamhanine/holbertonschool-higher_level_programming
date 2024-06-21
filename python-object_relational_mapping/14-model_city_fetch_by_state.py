#!/usr/bin/python3
"""
This script prints all City objects from
the database hbtn_0e_14_usa:
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and delete state
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    instance = session.query(City, State).join(State).order_by(City.id)

    for _c, _s in instance.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))

    session.commit()
    session.close()
