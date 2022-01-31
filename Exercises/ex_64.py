"""
Create class ComputerPeripheral that can be initialized using constructor.
Properties of the class:
- brand
- model

Create class Mouse that inherits class ComputerPeripheral and can be initialized using constructor.
Properties of the class:
- dpi (int)
- is_bluetooth (bool)
- number_of_buttons (int)

Create class Keyboard that inherits class ComputerPeripheral and can be initialized using constructor.
Properties of the class:
- is_wireless (bool)
- is_full_size (bool)
- compatibile_os (list of strings, like "Windows", "Linux", "OS X", "Android")

Create one Instance of Mouse and one instance of Keyboard.
Add both instances to list.
Loop through the list and print brand and model of each instance.
"""
class ComputerPeripheral:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Mouse(ComputerPeripheral):
    def __init__(self, brand, model, dpi, is_bluetooth, number_of_buttons):
        super().__init__(brand, model)
        #Same thing: ComputerPeripheral.__init__(self, brand, model)

        self.dpi = int(dpi)
        self.is_bluetooth = bool(is_bluetooth)
        self.number_of_buttons = int(number_of_buttons)

class Keyboard(ComputerPeripheral):
    def __init__(self, brand, model, is_wireless, is_full_size, compatibile_os):
        super().__init__(brand, model)
        #Same thing: ComputerPeripheral.__init__(self, brand, model)

        self.is_wireless = bool(is_wireless)
        self.is_full_size = bool(is_full_size)
        self.compatibile_os = compatibile_os

mouse = Mouse("Super brand", "Cool Mouse", 4000, True, 5)
keyboard = Keyboard("Super brand", "Flagship Keyboard", True, True, ["Windows", "Linux"])

list = []
list.append(mouse)
list.append(keyboard)

for item in list:
    print(f"{item.brand} - {item.model}")
