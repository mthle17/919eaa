"""
Improve the last example.
In the class Street, create the list of houses that will hold 
all the houses in the street.
In the class street, create add_house() method that will add 
the house to that list by calling: add_house(number).

Print data by iterating through streets.

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
        self.houses = []

    def __repr__(self):
        return f"{self.name}, {self.city}"

    def add_house(self, number):
        house = House(self, number)
        self.houses.append(house)

class House:
    def __init__(self, street, number):
        self.street = street
        self.number = int(number)

    def __repr__(self):
        return f"Nr. {self.number}"

streets = []
street1 = Street("Ilica", "Zagreb")
street1.add_house(1)
street1.add_house(2)
streets.append(street1)

street2 = Street("Vukovarska Avenija", "Zagreb")
street2.add_house(10)
street2.add_house(12)
streets.append(street2)

# Just go through all the streets and houses that are part of them
for street in streets:
    for house in street.houses:
        print(f"{house} ({street})")
