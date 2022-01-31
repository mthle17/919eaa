import requests
from requests.models import HTTPError

base = 'https://restcountries.com/v3.1/name/'

while True:
    country = input("Enter country name: ")
    if country == "exit":
        break

    country = country.replace(" ", "%20")
    url = base + country

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()

        for state in data:
            print(f"{state['cca3']} -> {state['capital']}.")

    except HTTPError as http_err:
        print(f"HTTP error, request failed: {http_err}")
    except Exception as err:
        print(f"Request failed: {err}")
