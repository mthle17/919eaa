"""
Create a class House.
Class has to be able to store value "number" inside.
Write a method set_number() to set that value.
Write a method get_number() to get that value.

Then:
- instance that class
- set the house number to '5a'
- get the house number and store into the local variable
- print the house number like this: "House number {num}"
"""
class House:
    def set_number(self, house_number):
        self.number = house_number
    
    def get_number(self):
        return self.number

my_house = House()
my_house.set_number(5)
num = my_house.get_number()
print(f"House number {num}")
