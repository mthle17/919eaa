"""
Let days of week be a list.
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

Let prediction also be a list
predictions = ["sunny", "rainy", "foggy", "cold", "freezing cold", "hot",  "scorching hot"]

Create a function that writes out a statement about the weather:
Function takes a random item from the first and the second list and uses them to create a sentence.
    Next [day] it will be [prediction].

When program is run, function gets called.

*Example*
Next Friday it will be foggy.
"""
import random

def random_forecast():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    predictions = ["sunny", "rainy", "foggy", "cold", "freezing cold", "hot",  "scorching hot"]

    day = random.choice(days)
    prediction = random.choice(predictions)
    forecast = f"Next {day} it will be {prediction}."
    return forecast

forecast = random_forecast()
print(forecast)
