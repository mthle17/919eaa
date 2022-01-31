"""
Create a class ComputerMouse.
Class must have the following fields:
- brand (string)
- model (string)
- is_bluetooth (bool)
- weight (int)
- dpi (int)
- number_of_buttons (int)
- free_wheel (bool)

All fields should be set in a constructor.
Default values are:
- is_bluetooth: False
- free_wheel: False

Create three instances:
pc_mouse1 = ComputerMouse("Logitech", "MX Master 2S", 141, 4000, 8, True, True)
pc_mouse2 = ComputerMouse("Razer", "DeathAdder", 96, 6400, 5, False, True)
pc_mouse3 = ComputerMouse("Kensington", "Pro Fit", 204, 2400, 5)

Print brand, model and number of DPI for each of them.
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

pc_mouse1 = ComputerMouse("Logitech", "MX Master 2S", 141, 4000, 8, True, True)
pc_mouse2 = ComputerMouse("Razer", "DeathAdder", 96, 6400, 5, False, True)
pc_mouse3 = ComputerMouse("Kensington", "Pro Fit", 204, 2400, 5)

print(f"{pc_mouse1.brand} {pc_mouse1.model}: {pc_mouse1.dpi} DPI")
print(f"{pc_mouse2.brand} {pc_mouse2.model}: {pc_mouse2.dpi} DPI")
print(f"{pc_mouse3.brand} {pc_mouse3.model}: {pc_mouse3.dpi} DPI")
