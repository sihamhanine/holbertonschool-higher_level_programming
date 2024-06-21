#!/usr/bin/python3
"""
Defines module 7-model_state_fetch lists all State
objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    """
    Access to database and get all states
    from the database
    """
    # Récupérer les arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # Créer un moteur de connexion à la base de données MySQL
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@ \
    localhost:3306/{database}")

    # creer une session pour interagir avec bd
    Session = sessionmaker(bind=engine)

    session = Session()

    # Requête pour obtenir tous les objets State et les trier par id
    req = session.query(State).order_by(State.id).all()

    # afficher le resultat
    for state in req:
        print(f"{state.id}: {state.name}")
    # Fermer la session
    session.close()
