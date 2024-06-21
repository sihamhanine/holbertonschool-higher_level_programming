#!/usr/bin/python3
"""
This script changes the name of a State
object from the database hbtn_0e_6_us
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and change state
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    instance = session.query(State).filter(State.id == '2').first()
    instance.name = 'New Mexico'
    session.commit()
    session.close()
