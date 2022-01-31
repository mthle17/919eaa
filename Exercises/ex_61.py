"""
Create two classes: Street and House.

Class Street has following properties:
- name (string)
- city (string)
- initialize it using constructor
- string representation: "{name}, {city}"

Class House has following properties:
- street name (string)
- number (int)
- initialize it using constructor
- string representation: "{number}"

Instance 4 houses and 2 streets (two houses per street).
Houses have to be stored in a list of houses.
Streets have to be stored in a list of streets.

Write out all streets and all houses using loops.

*EXAMPLE*
Nr. 1 (Ilica, Zagreb)
Nr. 2 (Ilica, Zagreb)
Nr. 10 (Vukovarska Avenija, Zagreb)
Nr. 12 (Vukovarska Avenija, Zagreb)
"""
class Street:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __repr__(self):
        return f"{self.name}, {self.city}"

class House:
    def __init__(self, street_name, number):
        self.street_name = street_name
        self.number = int(number)

    def __repr__(self):
        return f"Nr. {self.number}"

streets = []
streets.append(Street("Ilica", "Zagreb"))
streets.append(Street("Vukovarska Avenija", "Zagreb"))

houses = []
houses.append(House("Ilica", 1))
houses.append(House("Ilica", 2))
houses.append(House("Vukovarska Avenija", 10))
houses.append(House("Vukovarska Avenija", 12))

# Go through all the streets
for street in streets:
    # For each street, go through all the houses
    for house in houses:
        # If house is in that street, print house and street
        if house.street_name == street.name:
            print(f"{house} ({street})")
