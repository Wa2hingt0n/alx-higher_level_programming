#!/usr/bin/python3
""" Prints the `State` object with the `name` of the state to
    be searched passed as an argument from the database `hbtn_0e_6_usa`.
    Results should display the state id or `Not found` if the state isn't found

    Usage: <9-model_state_filter_a.py> <username> <password> <database> <name>
"""


if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
