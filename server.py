from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension
import jinja2
from model import Happyhour, connect_to_db, db
import requests
from utils import send_api_request, send_api_request2, send_api_request3
from datetime import datetime
from pytz import timezone


app = Flask(__name__)
app.secret_key = 'pAsSworD123'
app.jinja_env.undefined = jinja2.StrictUndefined
# to make Debugging easier^

# Get today's day and time in CST
CST = timezone('US/Central')
now = datetime.now(CST)
now_day = now.weekday()
now_weekday = now.strftime('%A')
now_time = now.strftime("%-I:%M %p")


@app.route("/")
def index():
    """Returns the landing page if not logged in"""

    return render_template("landing.html")


@app.route("/results")
def show_results():
    """Returns page with all results"""

    user_location = request.args.get('input')

    # Location defaults to Minneapolis if not entered
    if user_location == "":
        user_location = "Minneapolis"

    yelp_response = send_api_request(user_location)
    yelp_businesses = yelp_response['businesses']

    # Append "happyhour" attribute to yelp response
    for yelp_business in yelp_businesses:
        yelp_business["happyhour"] = Happyhour.query.filter_by(yelp_id=yelp_business['id'], day=now_day).order_by(Happyhour.happyhour_id.desc()).first()

    # for i, yelp_business in enumerate(yelp_businesses):
    #     if Happyhour.query.filter_by(yelp_id=yelp_business['id']).first() == None:
    #         yelp_businesses.pop(i)
    #         pass

    return render_template("results.html", 
                           businesses=yelp_businesses,
                           user_location=user_location,
                           now_weekday=now_weekday,
                           now_time=now_time)    


@app.route("/search")
def search():
    """Searches for a specific restaurant"""

    user_search = request.args.get('search')
    user_location = request.args.get('user_location')

    yelp_response = send_api_request3(user_search, user_location)
    yelp_businesses = yelp_response['businesses']

    for business in yelp_businesses:
        happyhour = Happyhour.query.filter_by(yelp_id=business['id'], day=now_day).order_by(Happyhour.happyhour_id.desc()).first()
        business["happyhour"] = happyhour

    return render_template("results.html",
                            businesses=yelp_businesses,
                            user_location=user_location,
                            now_weekday=now_weekday,
                            now_time=now_time)


@app.route("/details/<yelp_id>")
def show_restaurant(yelp_id):
    """Shows details for each restaurant"""

    yelp_business = send_api_request2(yelp_id)

    week = []

    for i in range(7):
        week.append(Happyhour.query.filter_by(yelp_id=yelp_id, day=i).order_by(Happyhour.happyhour_id.desc()).first())

    monday, tuesday, wednesday, thursday, friday, saturday, sunday = week

    # monday = Happyhour.query.filter_by(yelp_id=yelp_id, day=0).order_by(Happyhour.happyhour_id.desc()).first()
    # tuesday = Happyhour.query.filter_by(yelp_id=yelp_id, day=1).first()

    return render_template("details.html", 
                            yelp_business=yelp_business,
                            monday=monday,
                            tuesday=tuesday,
                            wednesday=wednesday,
                            thursday=thursday,
                            friday=friday,
                            saturday=saturday,
                            sunday=sunday)


@app.route("/submit/<yelp_id>")
def submit_form(yelp_id):

    business_name = request.args.get('business_name')

    week = {0 : 'Monday',
            1 : 'Tuesday',
            2 : 'Wednesday', 
            3 : 'Thursday', 
            4 : 'Friday', 
            5 : 'Saturday', 
            6 : 'Sunday'}

    return render_template("form.html",
                           week=week,
                           yelp_id=yelp_id,
                           business_name=business_name)


@app.route("/thankyou", methods = ['POST'])
def thank_user():
    """Retrieves data from form.html"""

    for item in request.form.lists():
        print(item)

    for i in range(7):

        yelp_id = request.form.getlist("yelp_id")[0]
        day = request.form.getlist("day")[i]
        start_time = request.form.getlist("start_time")[i]
        end_time = request.form.getlist("end_time")[i]
        # if end_time == 'Null':
        # end_time = None

        if start_time != 'Null' and end_time != 'Null':

            happyhour = Happyhour(yelp_id=yelp_id,
                                  day=day,
                                  start_time=start_time,
                                  end_time=end_time)

            db.session.add(happyhour)
     
    db.session.commit()

    print(f'Successfully added: {yelp_id}')

    return redirect(url_for('show_restaurant', yelp_id=yelp_id))


if __name__ == "__main__":
    # so that the server can connect to the database
    # in addition to the one in model.py
    connect_to_db(app)

    app.run(debug=True, host="0.0.0.0")

    
