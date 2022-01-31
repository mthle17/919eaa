"""
Create a function that takes a text and a number.
If text length is longer than the number given, it returns number of asterisks that is equal to number of characters.
Otherwise it returns the original text.

When program is run, user must enter the text and the number and then the function gets called.

*Example*
Please enter text: Hello world
Please enter number: 20
Hello world

*Example*
Please enter text: Hello world
Please enter number: 5
***********
"""
def mangle(text, number):
    if(len(text) > number):
        return "*" * len(text)
    else:
        return text

text = input("Please enter text: ")
number_str = input("Please enter number: ")
number = int(number_str)
mangled_text = mangle(text, number)
print(mangled_text)
