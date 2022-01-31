"""
Write a program that writes table of multiplication data to CSV file.
Format of the row is: number1,number2,multiplied_result
There have to be 100 rows in the CSV file.
File must be named data.csv

Protect the program against the error.
If any error occurs, print message "Writing CSV failed".

*EXAMPLE*
1,1,1
1,2,2
1,3,3
1,4,4
1,5,5
1,6,6
1,7,7
1,8,8
1,9,9
1,10,10
2,1,2
2,2,4
2,3,6
2,4,8
...
10,8,80
10,9,90
10,10,100
"""
import os
import csv

# Let's check the current working directory...
print(os.getcwd())

try:
    # Open local file
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")

        for i in range(1, 11):
            for j in range(1, 11):
                writer.writerow([i, j, i*j])
        
        file.flush()


except Exception as err:
    print(f"Writing CSV failed")
