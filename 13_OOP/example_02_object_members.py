class Square:
    def print_hello (self):
        self.message = "Square"
        print(self.message)

sq = Square()
#print(sq.__dict__) # Nothing was created after instantiation, so this will be empty
sq.print_hello()

sq.pi = 3.14
sq.something_else = "text 123"
print(sq.__dict__) # Will show 'pi' attr
