import os

import requests

## INITIAL TESTS
# API base url (development purpose only. base url in production "tier.app/")
base_url = 'http://localhost:8000/'
app_base_url = 'yun.ir/'

# Testing the default django initial set up
# response = requests.get(base_url)
# assert 'Django: the Web framework' in response.text

## USER STORY
shorten_url = os.path.join(base_url, 'shorten-url/')

# the user send post request to endpoint /shorten-url
# post request include url to be shortened
original_url = 'https://www.time.ir/'
payload = {'url': original_url}

response = requests.post(shorten_url, data=payload)
# user then receives a response with the shorten url containing "tier.app/"
# as base url with the unique shorten url id
# (it be better) if only the short id is sent.
assert response.status_code == 201

# print(response.text)
short_url = response.json()['short_id']
short_id = short_url.replace(app_base_url, '')
assert app_base_url in short_url

# then user is able to request the original url with shorten url
get_request_url = os.path.join(base_url, short_id)
response = requests.get(get_request_url)

# the the user should receive the original
url = response.json()['url']
assert original_url == url
