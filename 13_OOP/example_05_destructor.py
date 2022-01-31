class Square:
    def __init__(self, length = 3):
        self.length = length

    def __del__(self):
        print("I'm just being deleted by GC :(")

sq1 = Square()
sq2 = Square(7)

# OUTPUT ON PROGRAM EXIT: "I'm just being deleted by GC :(" x2
