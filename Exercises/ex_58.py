"""
Use a class ComputerMouse that you created in last exercise.
For the class, override method __str__ that will return
string representation of the class like brand, model and 
number of DPI.

When instancing, don't use separate variables, but add each of the 
instances to the list.
At the end, use lop to print string representations for all classes 
in that list.
"""
class ComputerMouse:
    def __init__(self, 
        brand, model, weight, dpi, number_of_buttons, 
        is_bluetooth = True, free_wheel = False):

        self.brand = brand
        self.model = model
        self.weight = int(weight)
        self.dpi = int(dpi)
        self.number_of_buttons = int(number_of_buttons)
        self.is_bluetooth = bool(is_bluetooth)
        self.free_wheel = bool(free_wheel)

    def __str__(self):
        return f"{self.brand} {self.model}: {self.dpi} DPI"


pc_mice = []
pc_mice.append(ComputerMouse("Logitech", "MX Master 2S", 141, 4000, 8, True, True))
pc_mice.append(ComputerMouse("Razer", "DeathAdder", 96, 6400, 5, False, True))
pc_mice.append(ComputerMouse("Kensington", "Pro Fit", 204, 2400, 5))

for pc_mouse in pc_mice:
    print(pc_mouse)
