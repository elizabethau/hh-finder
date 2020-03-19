from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

import jinja2
#jinja is a template system for python

from model import Happyhour, connect_to_db, db
#importing our Database 

import requests

from utils import send_api_request, send_api_request2
# for API use

from datetime import date


app = Flask(__name__)


app.secret_key = 'pAsSworD123!!!!'


app.jinja_env.undefined = jinja2.StrictUndefined
# to make Debugging easier^



@app.route("/")
def index():
    """Returns the landing page if not logged in"""

    return render_template("landing.html")


@app.route("/results")
def show_results():
    """Returns page with top 10 results"""

    user_location = request.args.get('input')

    # location defaults to Minneapolis if not entered
    if user_location == "":
        user_location = "Minneapolis, MN"


    # yelp_response is a dictionary of dictionaries
    yelp_response = send_api_request(user_location)
    yelp_businesses = yelp_response['businesses']

    day_int = date.today().weekday()
    day_str = date.today().strftime('%A')

    for business in yelp_businesses:

        happyhour = Happyhour.query.filter_by(yelp_id=business['id']).first()
        business["happyhour"] = happyhour


    return render_template("results.html", 
                           businesses=yelp_businesses,
                           user_location=user_location,
                           day_str=day_str)    


@app.route("/details/<yelp_id>")
def show_restaurant(yelp_id):
    """Displays restaurant details"""

    yelp_response = send_api_request2(yelp_id)
    
    happyhour = Happyhour.query.filter_by(yelp_id=yelp_id).first()

    return render_template("details.html", 
                            yelp_response=yelp_response,
                            happyhour=happyhour)


@app.route("/submit")
def submit_new():

    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    return render_template("form.html",
                           week=week)


if __name__ == "__main__":
    # so that the server can connect to the database
    # in addition to the one in model.py
    connect_to_db(app)

    app.run(debug=True, host="0.0.0.0")

    
