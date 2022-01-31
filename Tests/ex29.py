import os 
import csv

try:

    with open("multiplication.csv", "w", newline="") as document:
        writer = csv.writer(document, delimiter=",")

        for i in range(1,11):
            for j in range(1,11):
                writer.writerow([i,j,i*j])

        document.flush()

except Exception as err:
    print("Writing error")