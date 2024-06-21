#!/usr/bin/python3
"""
Defines module 6-model_state that contains the class
definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import sys


Base = declarative_base()


class State(Base):
    """
    create class state inherits from class Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name =  Column(String(128), nullable=False)

if __name__ == "__main__":
    host = "localhost"
    #create an engine
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@{host}:3306/{sys.argv[3]}", pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)
