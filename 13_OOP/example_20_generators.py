class FiboCollection:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.counter = 0
        self.a = 0
        self.b = 1
        return self
    
    def __next__(self):
        if self.counter >= self.n:
            raise StopIteration
        
        self.counter += 1
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b

        return result
    
fibo = FiboCollection(10)
for f in fibo:
    print(f, end=" ")
