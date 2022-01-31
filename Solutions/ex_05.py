"""
Write a program that asks for three numbers and writes out their sum.
If any of the inputs aren't numbers, write "Not a number" and exit.

*Example*
Please enter first number: 3
Please enter second number: 4
Please enter third number: 5
12
"""
first = input("Please enter first number: ")
if not first.isnumeric():
    print("Not a number")
    exit()

second = input("Please enter second number: ")
if not second.isnumeric():
    print("Not a number")
    exit()

third = input("Please enter second number: ")
if not third.isnumeric():
    print("Not a number")
    exit()

sum_of_numbers = int(first) + int(second) + int(third)
print(sum_of_numbers)
