from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
                             
# db.Model class is required for SQLAlchemy, do not need __init__() method

class Restaurant(db.Model):

    __tablename__ = "restaurants"

    restaurant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    yelp_id = db.Column(db.String, unique=True)
    name = db.Column(db.String)

    def __repr__(self):

        return f"<Restaurant {self.restaurant_id} = {self.name}>"


class Happyhour(db.Model):

    __tablename__ = "happyhours"

    happyhour_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants"))
    yelp_id = db.Column(db.String)
    day = db.Column(db.Integer)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    

    restaurant = db.relationship("Restaurant", backref="happyhours")

    # restaurant.happyhours - list of happy hours

    
    def __repr__(self):

        return f"{self.start_time} to {self.end_time}"


def connect_to_db(app):
    """Connect database to Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hhdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to database.")

