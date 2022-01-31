class ISound:
    def sound(self):
        pass

class Human(ISound):
    def sound(self):
        print("Hi there")

class Dog(ISound):
    def sound(self):
        print("Woof!")

class Cat(ISound):
    def sound(self):
        print("Meow!")

h = Human()
h.sound()

d = Dog()
d.sound()

c = Cat()
c.sound()
