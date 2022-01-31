"""
Create program that asks a user for his name and says hello.

*Example*
Please enter your name:     John   
Hello John!
"""
input_name = input("Please enter your name: ")
input_stripped = input_name.strip()
print(f"Hello {input_stripped}!")
