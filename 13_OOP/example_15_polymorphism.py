class PowerOf:
    def calc(self, x):
        self.x = x

class Square(PowerOf):
    def calc(self, x):
        #super().calc(x)
        return x**2

class Cubic(PowerOf):
    def calc(self, x):
        #super().calc(x)
        return x**3

l = [Square(), Cubic()]
for f in l:
    print(f.calc(5))
