"""
Write a program that connects to the endpoint and retrieves data from it.
Endpoint: http://localhost:8888/apparel

Returned data is of JSON format.
Write data to report.json file.

Protect the program against the error.
If any error occurs, print message "Report failed".

HINT:
(1) Run json_server.py from terminal (python ./utils/json_server.py)
(2) Check in browser if the endpoint is working
"""
import requests
import json

try:
    url = 'http://localhost:8888/apparel'
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    with open("report.json", "w") as file:
        json.dump(data, file)

except Exception as err:
    print(f"Report failed")
