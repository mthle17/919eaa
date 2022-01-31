"""
Write a program that connects to the endpoint and reads/writes data from/to it.
Endpoint: http://localhost:8888/apparel/1

Returned data is of JSON format, and contains following data:
- 'id' (product internal id) 
- 'name' (product name) 
- 'category' (product category)
- 'price' (product price)
- 'stock' (product stock)

Write two functions:

- get_product(id) 
  Function should call the endpoint using GET method with the id value appended.
  It should return 'stock' value from JSON response.
  Example: http://localhost:8888/apparel/1

- set_product(id, stock) 
  Function should call the endpoint using PUT method with the id value appended.
  Also, parameter 'stock' should be sent with form data.
  Example: http://localhost:8888/apparel/1

Program runs in endless loop.
It first asks for apparel id.
When user enters the number, it calls get_product(id) and displays the result.

It then asks for new stock value.
When user enters the number, it calls set_product(id, stock) and displays 'DONE' if update was successful.
Then it repeats the loop.

Program should take care of the leading/trailing spaces in input, meaning that input "   1  " should also be valid.
If anything goes wrong, programs should display 'ERROR' and exit.

HINT:
(1) Run json_server.py from terminal (python ./utils/json_server.py)
(2) Check in browser if the endpoint is working

*EXAMPLE*
Please enter the product id: 1
Stock: 5
Please enter the new stock value: 15
DONE
Please enter the product id: 1
Stock: 15
"""
import requests

def get_product(id):
    url = f'http://localhost:8888/apparel/{id}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    stock = data['stock']

    return stock

def set_product(id, stock):
    url = f'http://localhost:8888/apparel/{id}'
    new_data = {'stock':stock}
    response = requests.put(url, data=new_data)
    response.raise_for_status()

while(True):
    try:
        id = input("Please enter the product id: ")
        id = id.strip()
        stock = get_product(id)
        print(f"Stock: {stock}")

        stock = input("Please enter the new stock value: ")
        stock = stock.strip()
        set_product(id, stock)
        print(f"DONE")
    except Exception as err:
        print(f"ERROR")
        exit()
