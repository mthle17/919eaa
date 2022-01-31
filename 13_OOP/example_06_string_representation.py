class Square:
    def __init__(self, length = 3):
        self.length = length

    def __str__(self):
        """
        This method is called on print() or str()
        """
        return f"Square with a side of {self.length}"

sq1 = Square()
sq2 = Square(7)

# print(str(sq1))

print(sq1) # Short for print(str(sq1))
# print(sq2) # Short for print(str(sq2))

# For the next example:

# This will fail
sq3 = sq1 + sq2

# These will also fail
#print(sq1 < sq2)
#squares = [sq2, sq1, sq3]
#squares.sort()
