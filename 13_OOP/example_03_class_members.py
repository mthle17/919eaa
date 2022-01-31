class Square:
    name = 'Square' # Static attribute

    def print_hello ():
        # Static method can access a static attribute
        print(f"A static *hello* from {Square.name}")

Square.print_hello() # Call to the class (static) method

print(Square.name) # Static attribute access

sq = Square()
print(sq.name) # This also works
