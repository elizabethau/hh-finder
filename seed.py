from sqlalchemy import func
from model import Happyhour, connect_to_db, db


def load_businesses():
    """Load businesses into database"""

    for row in open("seed_data/test"):
        row = row.rstrip()
        happyhour_id, yelp_id, start_time, end_time, day = row.split("|")

        happyhour = Happyhour(happyhour_id=happyhour_id,
                              yelp_id=yelp_id,
                              day=day,
                              start_time=start_time,
                              end_time=end_time,
                              )

        db.session.add(happyhour)

    db.session.commit()


def set_val_happyhour_id():
    """Set value for the next happyhour_id after seeding database"""

    result = db.session.query(func.max(Happyhour.happyhour_id)).one()
    max_id = int(result[0])

    # Set the value for the next happyhour_id to be max_id + 1
    query = "SELECT setval('happyhours_happyhour_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    # create the tables
    db.create_all()
    set_val_happyhour_id()
    # Import data here
    load_businesses()
    