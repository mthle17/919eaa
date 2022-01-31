"""
Create program that asks for a word.
Output the word with first letter uppercase and the rest of letters lowercase.
Then output the word all in uppercase, and then in lowercase.

*Example*
Please enter a word: hElLo
Hello
HELLO
hello

"""
input_str = input("Please enter a word: ")
print(input_str.title())
print(input_str.upper())
print(input_str.lower())
