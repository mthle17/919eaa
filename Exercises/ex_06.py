"""
Write a program that sums up to N numbers.
N (number count) should be asked upfront.
If any of the inputs aren't numbers, write "Not a number" and exit.

*Example 1*
Please enter count of numbers to sum up: 4
Please enter number 1: 10 
Please enter number 2: 20
Please enter number 3: 30
Please enter number 4: 40
Result is 100

*Example 2*
Please enter count of numbers to sum up: 4
Please enter number 1: 10
Please enter number 2: X
Not a number

*Example 3*
Please enter count of numbers to sum up: Y
Not a number
"""
def GetNumber(input_text):
    str_in = input(input_text)
    if(not str_in.isnumeric()):
        print("Not a number")
        exit()
    num_in = int(str_in)
    return num_in

number_count = GetNumber("Please enter count of numbers to sum up: ")
sum = 0
for i in range(0, number_count):
    number = GetNumber(f"Please enter number {i + 1}: ")
    sum = sum + number
print(f"Result is {sum}")