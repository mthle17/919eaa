import requests
from requests.models import HTTPError

try:
    url = 'https://www.google.com/'
    response = requests.get(url)

    response.raise_for_status() # ensure error is raised for 400 <= code <= 600
    
    print("-"*25)
    print(response.headers)
    print("-"*25)
    print(response.text[0:100])
    print("-"*25)

except HTTPError as http_err:
    print(f"HTTP error, request failed: {http_err}")
except Exception as err:
    print(f"Request failed: {err}")
