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

    user_input = request.args.get('input')

    if user_input == "":
        user_input = "Minneapolis, MN"


    yelp_response = send_api_request(user_input)


    businesses = yelp_response['businesses']
    # name = data['businesses'][i]['name']
    # address = data['businesses'][i]['location']['display_address']


    return render_template("results.html", 
                           businesses=businesses,
                           user_input=user_input)    


@app.route("/details/<yelp_id>")
def show_restaurant(yelp_id):
    """Displays restaurant details"""

    yelp_response = send_api_request2(yelp_id)

    business = Happyhour.query.filter_by(yelp_id=yelp_id).all()

    return render_template("details.html", 
                            yelp_response=yelp_response,
                            business=business.start)


@app.route("/submit")
def submit_new():

    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    return render_template("form.html",
                           week=week)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
