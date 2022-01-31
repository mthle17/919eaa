"""
Write a program that reads data from CSV file and prints it.
File is named users.csv
Format of the row is: id,name,username,email,company,lat,long,apiKey,role,lastUpdate
For each row print the following info:

    ***User: {name}***
    Name: {username}
    Email: {email}

Protect the program against the error.
If any error occurs, print message "Reading CSV failed".

*EXAMPLE*
***User: Browning Delaney***
Name: browning94
Email: browning_delaney@assistix.furniture

***User: Tonia Weaver***
Name: tonia89
Email: tonia_weaver@retrack.cool
"""
import os
import csv

# Let's check the current working directory...
print(os.getcwd())

try:
    # Open local file
    with open("Exercises/users.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            print(f"***User: {row[1]}***")
            print(f"Name: {row[2]}")
            print(f"Email: {row[3]}")
            print()

except Exception as err:
    print(f"Reading CSV failed")
