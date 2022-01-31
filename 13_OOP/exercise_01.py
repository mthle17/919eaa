# Task:
class Street:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other: object) -> bool:
        if self.id == other.id:
            return True
    
    def __lt__(self, other: object) -> bool:
        return self.name < other.name

    def __str__(self) -> str:
        return f"{self.name}"

class Construction:

    def __init__(self, street, houseNumber, addition = None) -> None:
        self.street = street
        self.houseNumber = houseNumber
        self.addition = addition

    def __eq__(self, other: object) -> bool:
        if self.street == other.street and self.houseNumber == other.houseNumber and self.addition == other.addition:
            return True
    
    def __lt__(self, other: object) -> bool:
        if self.street == other.street:
            if self.houseNumber == other.houseNumber and self.addition != None:
                if self.addition == other.addition:
                    return False
                else:
                    return self.addition < other.addition
            else:
                return self.houseNumber < other.houseNumber
        else:
            return self.street < other.street

    def __str__(self) -> str:
        return f"{self.street} {self.houseNumber}{self.addition}"

class House(Construction):
    
    def __init__(self, street, houseNumber, addition = None) -> None:
        super().__init__(street, houseNumber, addition)

    def __str__(self) -> str:
        return f"House: {self.street} {self.houseNumber}" if self.addition == None else f"House: {self.street} {self.houseNumber}{self.addition}"

class School(Construction):

    def __init__(self, street, houseNumber, addition = None) -> None:
        super().__init__(street, houseNumber, addition)

    def __str__(self) -> str:
        return f"*** SCHOOL: {self.street} {self.houseNumber} ***" if self.addition == None else f"*** SCHOOL: {self.street} {self.houseNumber}{self.addition} ***"

class Building(Construction):

    def __init__(self, street, houseNumber, addition = None) -> None:
        super().__init__(street, houseNumber, addition)

    def __str__(self) -> str:
        return f"BUILDING: {self.street} {self.houseNumber}" if self.addition == None else f"BUILDING: {self.street} {self.houseNumber}{self.addition}"

if __name__ == "main":
    print("Start main!")
    exit

streets = [
    Street(0, "Ilica"),
    Street(1, "Vukovarska"),
    Street(2, "Ljubljanska"),
    Street(3, "Radnička")]

constructions = [
    House(streets[0], 54, "a"),
    Building(streets[1], 1),
    House(streets[1], 17),
    House(streets[1], 10),
    Building(streets[1], 18, "a"),
    Building(streets[1], 18, "b"),
    School(streets[2], 123),
    House(streets[3], 10)]

constructions.sort()

for c in constructions:
    print(c)
