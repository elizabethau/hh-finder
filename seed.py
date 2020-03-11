from sqlalchemy import func

from model import HappyHour, Restaurant, connect_to_db, db

from server import app

def load_restaurants():
    """Load restaurants into database"""

    app.logger.info('test here')


if __name__ == "__main__":
    connect_to_db(app)

    # create the tables
    db.create_all()

    # Import data here
    # load_restaurants()