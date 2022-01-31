class Square:
    def __init__(self, length_input):
        """
        Constructor
        """
        if length_input <= 0:
            print("Side <= 0!")

        self.length = length_input

sq1 = Square() # Call to a constructor method with missing parameter that is replaced by default
print(sq1.length)

sq2 = Square(7) # Call to a constructor method
print(sq2.length)

sq1 = Square(-5)
print(sq1.length)
