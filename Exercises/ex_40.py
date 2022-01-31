"""
Write a program that connects to endpoint to read the data
Endpoint: http://localhost:8888/user
Endpoint is protected by basic authentication (username: python, password: python)

Returned data is of JSON format, and each item contains following data:
- 'name' (user name)
- 'role' (user role in the system)

Program has to do the following:
- retrieve all users from the endpoint
- print text "Administrators:"
- for all users with role 'admin' and no company name print message "{user name}"

Protect the program against the error.
If any error occurs, print message "Execution failed".

HINT:
(1) Run json_server.py from terminal (python ./utils/json_server.py)
(2) Check in browser if the endpoint is working

*EXAMPLE*
***Administrators with missing company data***
Zamora Gibbs
Rosa Pearson
"""
import requests

try:
    # Read from endpoint
    base_url = 'http://localhost:8888/user'
    response = requests.get(base_url, auth=('python', 'python'))
    response.raise_for_status()
    users = response.json()

    # Write data to file, item by item
    print("***Administrators with missing company data***")
    for user in users:
        role = user['role']
        company = user['company']
        if(role == 'admin' and company == ''):
            name = user['name']
            print(name)

except Exception as err:
    print(f"Execution failed: {err}")
