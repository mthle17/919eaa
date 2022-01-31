"""
Improve the last example.
In the class House, instead of street name store the reference to the street.

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
    def __init__(self, street, number):
        self.street = street
        self.number = int(number)

    def __repr__(self):
        return f"Nr. {self.number}"

streets = []
houses = []

street1 = Street("Ilica", "Zagreb")
streets.append(street1)

houses.append(House(street1, 1))
houses.append(House(street1, 2))

street2 = Street("Vukovarska Avenija", "Zagreb")
streets.append(street2)

houses.append(House(street2, 10))
houses.append(House(street2, 12))

# Just go through all the houses
for house in houses:
    print(f"{house} ({house.street})")
