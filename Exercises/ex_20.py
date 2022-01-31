"""
Write a function that takes one number as an argument.
It prints its pairity: 'even' or 'odd'

When program is run, user must enter the number and the function gets called.

*EXAMPLE*
Please enter a number: 7
odd

*EXAMPLE*
Please enter a number: 2
even
"""
def pairity(number):
    if(number % 2 == 0):
        print("even")
    else:
        print("odd")

number = input("Please enter a number: ")
pairity(int(number))
