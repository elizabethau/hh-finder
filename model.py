from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# db.Model class is required for SQLAlchemy, do not need __init__() method
class HappyHour(db.Model):

    __tablename__ = "hh"

    rest_id = db.Column(db.Integer, db.ForeignKey('restaurant.rest_id'))
    hh_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start = db.Column(db.Integer, nullable = False)
    end = db.Column(db.Integer, nullable = False)
    day = db.Column(db.String(10), nullable = False)

    
    def __repr__(self):

        return f"HH is on {self.day} from {self.start} to {self.end}"


class Restaurant(db.Model):

    __tablename__ = "restaurant"

    rest_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(32), nullable = False)
    address = db.Column(db.String(56), nullable = False)
    menu = db.Column(db.String(500))


    def __repr__(self):

        return f"Restaurant: {self.name} is at {self.address}"



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
    print("Connected to DB mothafucka.")

