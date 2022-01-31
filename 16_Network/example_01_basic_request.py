import requests

response = requests.get('https://www.google.com/')
print(response.text[0:500])
