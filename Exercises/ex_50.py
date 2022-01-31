"""
Write a data visualization program that reads CSV file and shows values on a graph as bars.
File is named users.csv
Format of the row is: id,name,username,email,company,lat,long,apiKey,role,lastUpdate

Program should:
- read CSV file
- count number of users by role
- roles are: admin, read, read+write, reports
- display number of users by role using bars

Graph must be saved as user_roles.png
"""
import os
import csv
import matplotlib.pyplot as plt

# Let's check the current working directory...
print(os.getcwd())

try:
    roles = ['admin', 'read', 'read+write', 'reports']
    counts = [0, 0, 0, 0]

    # Open local file
    with open("Exercises/users.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            role = row[8] # role

            if(role == 'admin'):
                counts[0] = counts[0] + 1
            elif(role == 'read'):
                counts[1] = counts[1] + 1
            elif(role == 'read+write'):
                counts[2] = counts[2] + 1
            elif(role == 'reports'):
                counts[3] = counts[3] + 1

    plt.bar(roles, counts)
    plt.savefig('user_roles.png')
    plt.show()

except Exception as err:
    print(f"Creating bar chart failed")
