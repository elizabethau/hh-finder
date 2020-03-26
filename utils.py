import requests

payload = {}
headers = {
  'Authorization': 'Bearer NTAwKwdS4nSrXJxuv_wSsGmRyLse6bvFW-gECWO4Kvu20lmz8iKfsoA0Oix4MSJElLXw5LCHjgBiCIH8Z7OuEr-jgfy_yFZDzpaenyZvjy0H7BUWxuh62hk0IGdgXnYx'
}

# response = requests.request("GET", url, headers=headers, data = payload)


def send_api_request(user_input):

    url = "https://api.yelp.com/v3/businesses/search?location=" + user_input + "&categories=nightlife"

    # payload = {}
    # headers = {
    #   'Authorization': 'Bearer NTAwKwdS4nSrXJxuv_wSsGmRyLse6bvFW-gECWO4Kvu20lmz8iKfsoA0Oix4MSJElLXw5LCHjgBiCIH8Z7OuEr-jgfy_yFZDzpaenyZvjy0H7BUWxuh62hk0IGdgXnYx'
    # }

    response = requests.request("GET", url, headers=headers, data = payload)
    
    json_response = response.json()

    return json_response

def send_api_request2(yelp_id):

    url = "https://api.yelp.com/v3/businesses/" + yelp_id

    response = requests.request("GET", url, headers=headers, data = payload)

    json_response = response.json()

    return json_response

def send_api_request3(user_search, user_location):

    url = "https://api.yelp.com/v3/businesses/search?term=" + user_search + "&location=" + user_location + "&categories=nightlife"
    
    response = requests.request("GET", url, headers=headers, data = payload)

    json_response = response.json()

    return json_response

