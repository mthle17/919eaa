"""
Create a program that takes the following structures as an input:
    numbers = [3, 15, 6, 4, 11]
    calculations = ["+", "/", "*", "-"]

It takes numbers sequentially and calculates the following, 
according to calculations list:
    3 + 15 = 18
    18 / 6 = 3
    3 * 4 = 12
    12 - 11 = 1

For each operation it prints out the result.

Also, if length of numbers and length of calculations aren't matching correctly
it prints error and exits.

HINT: for division you can use operator // (floor, whole-number division)

*EXAMPLE*
numbers = [3, 15, 6, 4, 11]
calculations = ["+", "/", "*", "-"]
18
3
12
1

*EXAMPLE*
numbers = [3, 15, 6]
calculations = ["+", "/", "*", "-"]
Lengths don't match!
"""
numbers = [3, 15, 6, 4, 11]
calculations = ["+", "/", "*", "-"]

if(len(numbers) != len(calculations) + 1):
    print("Lengths don't match!")
    exit()

result = numbers[0]
for idx, number in enumerate(numbers):
    if idx == 0:
        continue

    if(calculations[idx - 1] == "+"):
        result = result + number
    elif(calculations[idx - 1] == "-"):
        result = result - number
    elif(calculations[idx - 1] == "*"):
        result = result * number
    elif(calculations[idx - 1] == "/"):
        result = result // number

    print(result)
