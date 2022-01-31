"""
Use last exercise as a starting point.
Don't initialize classes manually, but initialize them from the
following structure (list of dictionaries):
pc_mice_dict = [
    {
        BrandName: "Logitech",
        ModelName: "MX Master 2S",
        WeightInGrams: "141",
        MaxDpi: "4000",
        Buttons: "8",
        BT: "true",
        FreeWheel: "true"
    },
    {
        BrandName: "Razer",
        ModelName: "DeathAdder",
        WeightInGrams: "96",
        MaxDpi: "6400",
        Buttons: "5",
        BT: "false",
        FreeWheel: "true"
    },
    {
        BrandName: "Kensington",
        ModelName: "Pro Fit",
        WeightInGrams: "204",
        MaxDpi: "2400",
        Buttons: "5",
        BT: "false",
        FreeWheel: "false"
    }
]

At the end, in the loop write only mice that have DPI greater than 3000.
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

pc_mice_dict = [
    {
        "BrandName": "Logitech",
        "ModelName": "MX Master 2S",
        "WeightInGrams": "141",
        "MaxDpi": "4000",
        "Buttons": "8",
        "BT": "true",
        "FreeWheel": "true"
    },
    {
        "BrandName": "Razer",
        "ModelName": "DeathAdder",
        "WeightInGrams": "96",
        "MaxDpi": "6400",
        "Buttons": "5",
        "BT": "false",
        "FreeWheel": "true"
    },
    {
        "BrandName": "Kensington",
        "ModelName": "Pro Fit",
        "WeightInGrams": "204",
        "MaxDpi": "2400",
        "Buttons": "5",
        "BT": "false",
        "FreeWheel": "false"
    }
]

pc_mice = []
for item in pc_mice_dict:
    mouse = ComputerMouse(item["BrandName"], item["ModelName"], item["WeightInGrams"], 
        item["MaxDpi"], item["Buttons"], item["BT"], item["FreeWheel"])
    pc_mice.append(mouse)

for pc_mouse in pc_mice:
    if(pc_mouse.dpi > 3000):
        print(pc_mouse)
