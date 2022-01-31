"""
Write a program that connects to the endpoint and retrieves data from it.
Endpoint: http://localhost:8888/apparel

JSON data contains a list of items, and each item contains:
- 'name' (product name) 
- 'stock' (product stock)

For each item display product name and product stock data in the following way:
"Some Product Name: 5 in stock"

Protect the program against the error.
If any error occurs, print message "Execution failed".

HINT:
(1) Run json_server.py from terminal (python ./utils/json_server.py)
(2) Check in browser if the endpoint is working

*EXAMPLE*
Almond Toe Court Shoes, Patent Black: 5 in stock
Suede Shoes, Blue: 4 in stock
...
Bird Print Dress, Black: 10 in stock
Mid Twist Cut-Out Dress, Pink: 5 in stock
"""
import requests

try:
    url = 'http://localhost:8888/apparel'
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    for item in data:
        print(f"{item['name']}: {item['stock']} in stock")
except:
    print(f"Execution failed")

