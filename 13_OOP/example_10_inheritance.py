class Parent:
    __hidden = "hidden"
    exposed = "exposed"

    def classMethod():
        return "class method value"

    def objectMethod(self):
        return "object method value"

    def storeValue(self, val):
        self.objectValue = val

class Child(Parent):
    pass

child = Child()
child.storeValue(10) # (value stored into member variable)
print(child.objectValue) # 10
print(child.exposed) # exposed
print(child._Parent__hidden) # hidden
print(Child.classMethod()) # class method value
print(child.objectMethod()) # object method value
print(dir(child))
