"""
Write a program that connects to endpoints to read and write data.
Endpoint 1: http://localhost:8888/apparel
Endpoint 2: http://localhost:8888/apparel/1

Returned data is of JSON format, and each item contains following data:
- 'id' (product internal id) 
- 'name' (product name) 
- 'category' (product category)
- 'price' (product price)
- 'stock' (product stock)

First endpoint returns all product data. Call it using GET method.
Second endpoint deletes product data. Call it using DELETE method.
For each deleted product write one line in report.csv file.
Line must to contain all the product data.
If program is restarted, file shouldn't be overwritten - new lines should be added to it.

HINT:
(1) Run json_server.py from terminal (python ./utils/json_server.py)
(2) Check in browser if the endpoint is working

*EXAMPLE* (content of report.csv)
"""
import requests
import csv

try:
    # Read from endpoint
    base_url = 'http://localhost:8888/apparel'
    response = requests.get(base_url)
    response.raise_for_status()
    all_products = response.json()

    # Open local file
    file = open("report.csv", "a", newline="")
    writer = csv.writer(file, delimiter=",")

    # Write data to file, item by item
    for product in all_products:
        id = product['id']
        delete_url = f"{base_url}/{id}"
        response = requests.delete(delete_url)
        response.raise_for_status()

        datalist = [product['id'], product['name'], product['category'], product['price'], product['stock']]
        writer.writerow(datalist)
        file.flush()

except Exception as err:
    print(f"Report failed: {err}")
finally:
    file.close()
