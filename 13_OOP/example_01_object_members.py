class Square:
    """
    Class with an object method.
    """
    def print_hello (self):
        """
        Object method that writes a hello message.
        """
        print("Hello from Square")

sq = Square() # Create an object

sq.print_hello() # Call a method on an object

print(Square.__dict__) # List all methods and attributes

#Square.__dict__["print_hello"](sq) # Equivalent to k.print_hello()