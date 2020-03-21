from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
                             
# db.Model class is required for SQLAlchemy, do not need __init__() method

# class Restaurant(db.Model):

#     __tablename__ = "restaurants"

#     restaurant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     yelp_id = db.Column(db.String(50), unique=True)


class Business(db.Model):
    __tablename__ = 'businesses'

    business_id = db.Column(db.Integer, primary_key=True)
    yelp_id = db.Column(db.String, unique=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'<Business {self.id} | {self.name}>'


class Happyhour(db.Model):

    __tablename__ = "happyhours"

    happyhour_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses'))
    yelp_id = db.Column(db.String, unique=True)
    start = db.Column(db.Time)
    end = db.Column(db.Time)
    day = db.Column(db.Integer, nullable=False)

    business = db.relationship("Business", backref="happy_hours")

    def __repr__(self):

        return f"{self.start} to {self.end}"


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
    from flask import Flask
    # from server import app
    app = Flask(__name__)
    connect_to_db(app)
    db.create_all()
    print("Connected to database.")
