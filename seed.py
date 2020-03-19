from sqlalchemy import func
from model import Happyhour, connect_to_db, db




def load_businesses():
    """Load businesses into database"""

    print("test here")

    for row in open("seed_data/test"):
        row = row.rstrip()
        happyhour_id, yelp_id, start, end, day = row.split("|")

        happyhour = Happyhour(happyhour_id=happyhour_id,
                              yelp_id=yelp_id,
                              start=start,
                              end=end,
                              day=day)

        db.session.add(happyhour)

    db.session.commit()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    # create the tables
    db.create_all()

    # Import data here
    load_businesses()