class A:
    def show(self):
        print("Show from A")

class B:
    def show(self):
        print("Show from B")

    def say_hi(self):
        print("Hi from B")

class C(A, B):
    def say_hi(self):
        super().say_hi()
        print("Hi from C")

print(C.__mro__)
# C -> A -> B -> object

c = C()

c.say_hi()
# Hi from B  
# Hi from C  

c.show()
# Show from A
