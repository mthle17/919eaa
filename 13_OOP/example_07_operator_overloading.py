class Square:
    def __init__(self, length = 3):
        self.length = length

    def __str__(self):
        return f"Square with a side of {self.length}"

    def __add__(self, other):
        return Square(self.length + other.length)

    def __lt__(self, other):
        return self.length < other.length

sq1 = Square()
sq2 = Square(7)
sq3 = sq1 + sq2

print(sq3)
print(sq1 < sq2)

# Sorting
squares = [sq2, sq1, sq3]

print("Before sorting")
for sq in squares:
    print(sq)
    
squares.sort()

print("After sorting")
for sq in squares:
    print(sq)