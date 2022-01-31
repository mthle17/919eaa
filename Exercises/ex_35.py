"""
Write a program that connects to the endpoint and retrieves data from it.
Endpoint: http://localhost:8888/apparel

Returned data is of JSON format, and each item contains following data:
- 'id' (product internal id) 
- 'name' (product name) 
- 'category' (product category)
- 'price' (product price)
- 'stock' (product stock)

Write data to report.csv file.

Protect the program against the error.
If any error occurs, print message "Report failed".

HINT:
(1) Run json_server.py from terminal (python ./utils/json_server.py)
(2) Check in browser if the endpoint is working

*EXAMPLE* (content of report.csv)
1,"Almond Toe Court Shoes, Patent Black",Womens Footwear,99.0,5
2,"Suede Shoes, Blue",Womens Footwear,42.0,4
...
12,"Bird Print Dress, Black",Womens Formalwear,270.0,10
13,"Mid Twist Cut-Out Dress, Pink",Womens Formalwear,540.0,5
"""
import requests
import csv

try:
    # Read from endpoint
    url = 'http://localhost:8888/apparel'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Open local file
    with open("report.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")

        # Write data to file, item by item
        for d in data:
            datalist = [d['id'], d['name'], d['category'], d['price'], d['stock']]
            writer.writerow(datalist)

except Exception as err:
    print(f"Report failed")
