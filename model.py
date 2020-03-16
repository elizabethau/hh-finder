from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
                             

# db.Model class is required for SQLAlchemy, do not need __init__() method

# class Restaurant(db.Model):

#     __tablename__ = "restaurants"

#     restaurant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     yelp_id = db.Column(db.String(50), unique=True)


class Happyhour(db.Model):

    __tablename__ = "happyhours"

    happyhour_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    yelp_id = db.Column(db.String(50))
    # restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.restaurant_id"), nullable=False)
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)
    day = db.Column(db.Integer, nullable = False)

    # restaurant = db.relationship("Restaurant", backref="happyhours")

    
    def __repr__(self):

        return f"Happy hour on {self.day} is from {self.start} to {self.end}"


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

