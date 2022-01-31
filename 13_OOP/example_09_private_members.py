class Square:
    def __init__(self, length = 3):
        self.__length = length

    def __str__(self):
        return f"Length is {self.__length}"

sq = Square(5)
print(sq) # Length is 5

sq.__length = 8
print(sq) # Length is 5???

print(sq.__dict__)
