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
def get_number(question_text):
    n_str = input(question_text)
    if not n_str.isnumeric():
        print("Not a number")
        exit()
    return int(n_str)

that_many_times = get_number("Please enter count of numbers to sum up: ")
sum_of_values = 0
for val in range(1, that_many_times + 1):
    number = get_number(f"Please enter a number {val}: ")
    sum_of_values = sum_of_values + number
print(f"Result is {sum_of_values}")
