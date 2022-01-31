"""
Create three classes:
- class DataReporter
- class CsvReporter that inherits from DataReporter
- class JsonReporter that inherits from DataReporter

Methods of classes:
- DataReporter
    - report(name_part) - prints ids and names for users whose name contains name_part
    - load() - empty
- CsvReporter
    - load() - loads CSV file
- JsonReporter
    - load() - loads JSON file

Create instances of CsvReporter and JsonReporter.
Use CsvReporter to load CSV file and show result for name part "all".
Use JsonReporter to load JSON file and show result for the same name part.
Both results should be the same.

*EXAMPLE*
***CSV file report***
ca87a468-5280-4848-a993-98594c0a5b17: Randall Griffith
2ab2ee70-e5e3-4a77-a79b-3a3195e16519: Marion Wall
***JSON file report***
ca87a468-5280-4848-a993-98594c0a5b17: Randall Griffith
2ab2ee70-e5e3-4a77-a79b-3a3195e16519: Marion Wall
"""
import csv
import json

class DataManager:
    def __init__(self):
        """
        Initialize empty list of rows
        """
        self.data = []

    def report(self, name_part):
        """
        Look for data in the list of rows.
        """
        for item in self.data:
            if name_part in item[1]:
                print(f"{item[0]}: {item[1]}")
    
    def load():
        """
        Base class doesn't know how to load both JSON and CSV files.
        """
        pass

class CsvReporter(DataManager):
    def load(self):
        with open("Exercises/users.csv", "r") as file_in:
            csv_reader = csv.reader(file_in, delimiter=",")

            for row in csv_reader:
                self.data.append(row)

class JsonReporter(DataManager):
    def load(self):
        with open("Exercises/users.json", "r") as file_in:
            data = json.load(file_in)

            for item in data:
                row = [item["id"], item["name"]]
                self.data.append(row)

print("***CSV file report***")
csv_reporter = CsvReporter()
csv_reporter.load()
csv_reporter.report("all")

print("***JSON file report***")
json_reporter = JsonReporter()
json_reporter.load()
json_reporter.report("all")
