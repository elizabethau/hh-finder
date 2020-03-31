import requests

payload = {}
headers = {'Authorization': 'Bearer NTAwKwdS4nSrXJxuv_wSsGmRyLse6bvFW-gECWO4Kvu20lmz8iKfsoA0Oix4MSJElLXw5LCHjgBiCIH8Z7OuEr-jgfy_yFZDzpaenyZvjy0H7BUWxuh62hk0IGdgXnYx'}
base_url = "https://api.yelp.com/v3/businesses/"

#yelp_response is a dictionary of dictionaries

def send_api_request(user_input):

    url = base_url + "search?location=" + user_input + "&categories=bars"

    response = requests.request("GET", url, headers=headers, data = payload)

    return response.json()

def send_api_request2(yelp_id):

    url = base_url + yelp_id

    response = requests.request("GET", url, headers=headers, data = payload)

    return response.json()

def send_api_request3(user_search, user_location):

    url = base_url + "search?term=" + user_search + "&location=" + user_location + "&categories=bars"
    
    response = requests.request("GET", url, headers=headers, data = payload)

    return response.json()

