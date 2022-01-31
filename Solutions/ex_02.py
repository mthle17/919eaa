"""
Create program that asks a user for his name and says hello.

*Example*
Please enter your name:     John   
Hello John!
"""
name = input("Please enter your name: ")
name = name.strip()
print(f"Hello {name}!")
