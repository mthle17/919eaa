import requests

response = requests.get('https://www.google.com/')

if(response.status_code == 200):
    print("-"*25)
    print(response.headers)
    print("-"*25)
    print(response.text[0:100])
    print("-"*25)
else:
    print(f"Request failed, status code is: {response.status_code}")
