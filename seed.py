from sqlalchemy import func

from model import HappyHour, Restaurant, connect_to_db, db

from server import app

def load_restaurants():
    """Load restaurants into database"""

    r = Restaurant(rest_id = rest_id,
                   name = name,
                   address = address)

    app.logger.info('test here')

    db.session.add(r)

    db.session.commit()


## yelp code starts here
import requests

url = "https://api.yelp.com/v3/businesses/search?location=Minneapolis, Minnesota"

payload = {}
headers = {
  'Authorization': 'Bearer NTAwKwdS4nSrXJxuv_wSsGmRyLse6bvFW-gECWO4Kvu20lmz8iKfsoA0Oix4MSJElLXw5LCHjgBiCIH8Z7OuEr-jgfy_yFZDzpaenyZvjy0H7BUWxuh62hk0IGdgXnYx'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

## yelp code ends here

if __name__ == "__main__":
    connect_to_db(app)

    # create the tables
    db.create_all()

    # Import data here
    # load_restaurants()