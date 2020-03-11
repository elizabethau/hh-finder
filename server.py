from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

import jinja2
#jinja is a template system for python

from model import Restaurant, HappyHour, connect_to_db, db
#importing our Database 

import requests
# for API use

#yelp api starts yere
url = "https://api.yelp.com/v3/businesses/search?location=Minneapolis, Minnesota"

payload = {}
headers = {
  'Authorization': 'Bearer NTAwKwdS4nSrXJxuv_wSsGmRyLse6bvFW-gECWO4Kvu20lmz8iKfsoA0Oix4MSJElLXw5LCHjgBiCIH8Z7OuEr-jgfy_yFZDzpaenyZvjy0H7BUWxuh62hk0IGdgXnYx'
}

response = requests.request("GET", url, headers=headers, data = payload)
data = response.json()
# yelp api ends here

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

    businesses = data['businesses']
    # name = data['businesses'][i]['name']
    # address = data['businesses'][i]['location']['display_address']
    #list of dictionaries

    nu_list = []

    for business in businesses:
        nu_list.append(business['name'])

    return render_template("results.html", 
                           nu_list=nu_list)
    # return jsonify(nu_list)
    


@app.route("/place/<rest_id>")
def show_restaurant():
    """Displays restaurant details"""


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
