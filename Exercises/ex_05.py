"""
Write a program that asks for three numbers and writes out their sum.
If any of the inputs aren't numbers, write "Not a number" and exit.

*Example*
Please enter first number: 3
Please enter second number: 4
Please enter third number: 5
12
"""
str1 = input("Please enter first number: ")
if(not str1.isnumeric()):
    print("Not a number")
    exit()
num1 = int(str1)

str2 = input("Please enter second number: ")
if(not str2.isnumeric()):
    print("Not a number")
    exit()
num2 = int(str2)

str3 = input("Please enter third number: ")
if(not str3.isnumeric()):
    print("Not a number")
    exit()
num3 = int(str3)

result = num1 + num2 + num3
print(result)