"""
Create a class House.
Class has "number" member that is set by the constructor method.
Class has a string representation that is equal to letter "H" 
concatenated with the house number.

Enable the class to be sorted by numbers (additions are not allowed, just integers).
Use the following list to instance houses with numbers:
numbers = [3,4,6,9,10,5,11,12,8]

At the end, sort houses and write out original number list and sorted house list.

HINT: use __repr__() instead of __str__(), because collections use __repr__()
for string representation.

*EXAMPLE*
[3, 4, 6, 9, 10, 5, 11, 12, 8, 10]
[H3, H4, H5, H6, H8, H9, H10, H10, H11, H12]
"""
class House:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return "H" + str(self.number)

    def __lt__(self, other):
        return self.number < other.number

numbers = [3,4,6,9,10,5,11,12,8,10]
houses = []
for number in numbers:
    house = House(number)
    houses.append(house)

houses.sort()

print(numbers)
print(houses)
