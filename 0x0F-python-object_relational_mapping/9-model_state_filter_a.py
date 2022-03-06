#!/usr/bin/python3
""" Lists all `State` objects that contain the letter `a`
    from the database `hbtn_0e_6_usa`

    Usage: <9-model_state_filter_a.py> <username> <password> <database>
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

    for state in session.query(State).filter(State.name.ilike(
            "%a%")).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
