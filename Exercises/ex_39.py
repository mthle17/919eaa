"""
Write a program that connects to endpoints to read and write data.
Endpoint 1: http://localhost:8888/user
Endpoint 2: http://localhost:8888/user/1
Endpoint is protected by basic authentication (username: python, password: python)

Returned data is of JSON format, and each item contains following data:
- 'id' (in GUID form) 
- 'role' (user role in the system)

First endpoint returns all user data. Call it using GET method.
Second endpoint deletes user data. Call it using DELETE method.

You have to delete first 5 users that have the 'reports' role.
For each deleted user print the following line:
    "Deleted user id={id of user}, name={name of user}"

Protect the program against the error.
If any error occurs, print message "Delete failed".

HINT:
(1) Run json_server.py from terminal (python ./utils/json_server.py)
(2) Check in browser if the endpoint is working

*EXAMPLE*
Deleted user id=693f7c9f-488f-4136-a5dc-836d4a19e789, name=Parks Vargas
Deleted user id=dfd69811-53e1-42cf-9d38-76ca7e77d36d, name=Summers Roman
Deleted user id=e3a417d6-18bf-4255-98f0-97144e52fee5, name=Staci Parrish
Deleted user id=3284473e-f060-4c00-a0f1-524b9e9f567a, name=Misty Lawrence
Deleted user id=88a58182-2cc4-4a3f-9afe-088da6afe02a, name=Riley Wynn
Deleted user id=2ab2ee70-e5e3-4a77-a79b-3a3195e16519, name=Marion Wall
Deleted user id=207fb7e7-4cc8-4b2d-bb61-4dfbf677a217, name=Gail Riddle
Deleted user id=e06d9e92-5953-4a99-9522-f539480628bc, name=Clements Buckley
Deleted user id=9f596935-12ff-4924-a328-d8e8ffa85287, name=Marci Kelley
"""
import requests

try:
    # Read from endpoint
    base_url = 'http://localhost:8888/user'
    response = requests.get(base_url, auth=('python', 'python'))
    response.raise_for_status()
    all_users = response.json()

    # Write data to file, item by item
    for user in all_users:
        id = user['id']
        name = user['name']
        role = user['role']
        if(role == 'reports'):
            delete_url = f"{base_url}/{id}"
            response = requests.delete(delete_url, auth=('python', 'python'))
            print(f"Deleted user id={id}, name={name}")
            response.raise_for_status()

except Exception as err:
    print(f"Delete failed")
