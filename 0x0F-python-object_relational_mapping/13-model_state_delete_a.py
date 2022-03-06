#!/usr/bin/python3
""" Deletes all `State` objects from the database `hbtn_0e_6_usa`
    with a name containing the letter `a`

    Usage: <13-model_state_delete_a_.py> <username> <password>
"""


if __name__ == "__main__":

    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.ilike("%a%")):
        session.delete(state)

    session.commit()
