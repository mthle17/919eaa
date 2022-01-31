"""
Write a function that takes a number as an argument.
Function then loops from 1 to that number.
It prints 'one', 'two' and 'three' for groups of consecutive numbers.
E.g. for first three numbers it prints 'one', 'two' and 'three'. 
Then, for next three numbers it prints again 'one', 'two', and 'three' etc.

When program is run, user must enter the number and the function gets called.

*EXAMPLE*
Please enter a number: 7
1 - one
2 - two
3 - three
4 - one
5 - two
6 - three
7 - one
"""
def print_groups_of_3(number):
    for n in range(1, number + 1):
        if(n % 3 == 0):
            print(f"{n} - three")
        elif(n % 3 == 1):
            print(f"{n} - one")
        elif(n % 3 == 2):
            print(f"{n} - two")

number = input("Please enter a number: ")
print_groups_of_3(int(number))
