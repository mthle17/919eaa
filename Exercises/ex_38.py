"""
Write a program that connects to the endpoint and retrieves data from it.
Endpoint: http://localhost:8888/user
Endpoint is protected by basic authentication (username: python, password: python)

JSON data contains a list of items:
- 'id' (in GUID form) 
- 'name' (user first and last name)
- 'email' (user email)

For first five items display id, first name, last name and email in the following way:
"ea267d9b-ac29-4476-b500-427f57730c55: Browning Delaney, browning_delaney@assistix.furniture"

Protect the program against the error.
If any error occurs, print message "Report failed".

HINT:
(1) Run json_server.py from terminal (python ./utils/json_server.py)
(2) Check in browser if the endpoint is working

*EXAMPLE*
ea267d9b-ac29-4476-b500-427f57730c55: Browning Delaney, browning_delaney@assistix.furniture
2aee4d5e-91ea-418d-a18d-2fcdf2b113cb: Tonia Weaver, tonia_weaver@retrack.cool
693f7c9f-488f-4136-a5dc-836d4a19e789: Parks Vargas, parks_vargas@comtour.kw
a2af2182-b930-4f55-a20f-b9f7a762e725: Ayala Avila, ayala_avila@inrt.surf
dfd69811-53e1-42cf-9d38-76ca7e77d36d: Summers Roman, summers_roman@entogrok.wien
"""
import requests

try:
    url = 'http://localhost:8888/user'
    response = requests.get(url, auth=('python', 'python'))
    response.raise_for_status()
    
    data = response.json()
    for item in data[:5]:
        print(f"{item['id']}: {item['name']}, {item['email']}")
except:
    print(f"Request failed")
