class Parent:
    def __init__(self):
        self.calc_i(30)
        print(f"i from Parent is {self.i}")
    def calc_i(self, i):
        self.i = 2 * i

class SimpleChild(Parent):
    pass

class Child(Parent):
    def __init__(self):
        super().__init__()
        print(f"i from Child is {self.i}")
    def calc_i(self, i):
        self.i = 3 * i

p = Parent() # i from Parent is 60
sc = SimpleChild() # i from Parent is 60
c = Child()
# i from Parent is 90
# i from Child is 90

class Parent1:
    def calc1(self, value):
        do_something(value)

class Parent2:
    def calc2(self, value):
        do_something(value)

class Parent3:
    def calc3(self, value):
        do_something(value)

class Child(Parent1, Parent2, Parent3):
    pass