"""
Write a data visualization program that works exactly as ex_50, but uses matplotlib 
built-in histogram functionality.

Save the graph as user_roles_histogram.png.

NOTES:
 - to generate a histogram, you need all the role data in one list like
    ['admin', 'reports', 'admin', 'read+write', 'admin', 'reports', ...]
 - you need plt.hist() instead of plt.bar(), and send just list of items
   to the method .hist(), pyplot will calculate the rest
 - use additional bins parameter (how many bars should be displayed?): bins=4
 - use additional rwidth parameter (how wide should a bar appear?): rwidth=0.9
"""
import os
import csv
import matplotlib.pyplot as plt

# Let's check the current working directory...
print(os.getcwd())

try:
    role_instances = []

    # Open local file
    with open("Exercises/users.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            role = row[8] # role
            role_instances.append(role)

    plt.hist(role_instances, bins=4, rwidth=0.9)
    plt.savefig('user_roles_histogram.png')
    plt.show()

except Exception as err:
    print(f"Creating bar chart failed")
