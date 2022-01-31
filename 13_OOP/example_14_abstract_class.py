class Person:
    def __init__(self, name):
        self.name = name
    def which_gender(self):
        pass

class Female(Person):
    def which_gender(self):
        print("F") 

class Male(Person):
    def which_gender(self):
        print("M") 

f = Female("Jane")
f.which_gender()

m = Male("John")
m.which_gender()

p = Person("Unknown")
p.which_gender()
