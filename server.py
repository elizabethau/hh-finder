from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

import jinja2
#jinja is a template system for python

from model import Happyhour, connect_to_db, db
#importing our Database 

import requests

from utils import send_api_request, send_api_request2, send_api_request3
# for API use

from datetime import date, datetime


app = Flask(__name__)
app.secret_key = 'pAsSworD123'


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
    time = datetime.now().strftime("%I:%M %p")

    for business in yelp_businesses:

        happyhour = Happyhour.query.filter_by(yelp_id=business['id'], day=day_int).first()

        business["happyhour"] = happyhour

    return render_template("results.html", 
                           businesses=yelp_businesses,
                           user_location=user_location,
                           day_str=day_str,
                           time=time)    


@app.route("/search")
def search():
    """Searches for a specific restaurant"""

    user_search = request.args.get('search')
    user_location = request.args.get('user_location')

    yelp_response = send_api_request3(user_search, user_location)

    yelp_businesses = yelp_response['businesses']


    return render_template("search_results.html",
                            businesses=yelp_businesses,
                            user_search=user_search)


@app.route("/details/<yelp_id>")
def show_restaurant(yelp_id):
    """Shows details for each restaurant"""

    yelp_response = send_api_request2(yelp_id)


    monday = Happyhour.query.filter_by(yelp_id=yelp_id, day=0).first()
    tuesday = Happyhour.query.filter_by(yelp_id=yelp_id, day=1).first()
    wednesday = Happyhour.query.filter_by(yelp_id=yelp_id, day=2).first()
    thursday = Happyhour.query.filter_by(yelp_id=yelp_id, day=3).first()
    friday = Happyhour.query.filter_by(yelp_id=yelp_id, day=4).first()
    saturday = Happyhour.query.filter_by(yelp_id=yelp_id, day=5).first()
    sunday = Happyhour.query.filter_by(yelp_id=yelp_id, day=6).first()

    return render_template("details.html", 
                            yelp_response=yelp_response,
                            monday=monday,
                            tuesday=tuesday,
                            wednesday=wednesday,
                            thursday=thursday,
                            friday=friday,
                            saturday=saturday,
                            sunday=sunday)


@app.route("/submit/<yelp_id>")
def submit_form(yelp_id):


    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # week = [0, 1, 2, 3, 4, 5, 6]

    return render_template("form.html",
                           week=week,
                           place=yelp_id)

@app.route("/thankyou", methods = ['POST'])
def thank_user():

    # yelp_id = request.form.get('yelp_id')
    # start_time = request.form.get('start_time')
    # end_time = request.form.get('end_time')
    # day = request.form.get('day')
 
    for key, val in request.form.items():
        print (key, val)
     
        # happyhour = Happyhour(yelp_id=yelp_id,
        #                       day=day,
        #                       start_time=start_time,
        #                       end_time=end_time)

        # db.session.add(happyhour)

    # db.session.commit()

    # print(f'Successfully added: {yelp_id}')

    return 'Thank you'


if __name__ == "__main__":
    # so that the server can connect to the database
    # in addition to the one in model.py
    connect_to_db(app)

    app.run(debug=True, host="0.0.0.0")

    
