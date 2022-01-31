"""
Write a program that connects to the endpoint and retrieves data from it.
Endpoint: http://localhost:8888/apparel

JSON data contains a list of items, and each item contains:
- 'stock' (product stock)

Sum up total stock for all items and print out the result.

Protect the program against the error.
If any error occurs, print message "Request failed".

HINT:
(1) Run json_server.py from terminal (python ./utils/json_server.py)
(2) Check in browser if the endpoint is working

*EXAMPLE*
Total stock: 74
"""
import requests

stock_sum = 0

try:
    url = 'http://localhost:8888/apparel'
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    for item in data:
        stock = int(item['stock'])
        stock_sum = stock_sum + stock
except:
    print(f"Request failed")

print(f"Total stock: {stock_sum}")
