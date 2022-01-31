"""
Write a program that asks for a number in a loop and stores it into the list of numbers.
Loop ends when user enters something that is not a number (e.g. 'x').
If user enters leading spaces before the number, program should also treat the input as a number.
After loop exits, program prints:
(1) entire list of numbers
(2) all unique numbers from the list
(3) sum of all numbers

*EXAMPLE*
Please enter a number: 2
Please enter a number: 3
Please enter a number: 2
Please enter a number: 3
Please enter a number: 4
Please enter a number: quit
[2, 3, 2, 3, 4]
{2, 3, 4}
14
"""
num_list = []
while(True):
    input_str = input("Please enter a number: ")
    input_str = input_str.lstrip()
    if(not input_str.isnumeric()):
        break

    num = int(input_str)
    num_list.append(num)
    
print(num_list)

nums_unique = set(num_list)
print(nums_unique)

nums_sum = sum(num_list)
print(nums_sum)
