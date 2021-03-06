#!/usr/bin/python3
""" Adds the`State` object `Louisiana` to the database `hbtn_0e_6_usa` and
    prints its id.

    Usage: <11-model_state_insert.py> <username> <password>
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

    obj = State(name="Louisiana")
    session.add(obj)
    session.commit()

    state = session.query(State).filter(
        State.name == "Louisiana").first()

    print("{}".format(state.id))
