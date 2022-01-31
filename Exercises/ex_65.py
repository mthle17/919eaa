"""
Create class DataManager that can import some data from CSV file and export data to JSON file.

Class needs to have two methods:
- import_data() - imports data from existing file users.csv
                - format of the row is: id,name,username,email,company,lat,long,apiKey,role,lastUpdate
- export_data() - exports data to a new file users.json

Use that class to create users.json from users.csv.

NOTE: for deserialization, use json.dump() with parameter indent=2 to prettty-print the json file
"""
import csv
import json

class DataManager:
    def import_data(self):
        """
        Just read all the data into the list.
        """
        self.data = []
        with open("Exercises/users.csv", "r") as file_in:
            csv_reader = csv.reader(file_in, delimiter=",")

            for row in csv_reader:
                self.data.append(row)

    def export_data(self):
        """
        For each item in a list create a dictionary.
        Then put all the dictionaries into the list.
        And then serialize the list.
        """
        list = []
        for row in self.data:
            dict = {
                "id": row[0],
                "name": row[1],
                "username": row[2],
                "email": row[3],
                "company": row[4],
                "lat": row[5],
                "long": row[6],
                "apiKey": row[7],
                "role": row[8],
                "lastUpdate": row[9]
            }
            list.append(dict)
        
        with open("Exercises/users.json", "w") as file_out:
            json.dump(list, file_out, indent=2)

dm = DataManager()
dm.import_data()
dm.export_data()
