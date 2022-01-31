class CmpHash:

    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return self.a < other.a

    def __eq__(self, other):
        return self.a == other.a
    
    def __hash__(self):
        return hash(self.a) # Uses hash() function

    def __repr__(self):
        return str(self.a) # Uses str() function, meant for collection string-representation

t = {CmpHash(5), CmpHash(3), CmpHash(4)} # This is a set! Uses hash() and eq() for internal handling of members!
l = list(t)
l.sort()
print(l) # __repr__() will be called here