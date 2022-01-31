"""
Create functions that convert from cm to inch and from inch to cm.
Program should:
- ask for an input value and call the first function with that value as an argument
- print the result of conversion
- call the second function with that result as argument
- print the result

Take into account that input number can be decimal.

HINT: to convert from cm to inch, divide by 2.54

*EXAMPLE*
Length in inches: 0.39370078740157477
Length in cm: 0.9999999999999999
"""
def cm_to_inch(cms):
    return cms / 2.54

def inch_to_cm(inches):
    return inches * 2.54

number = input("Please enter length in cm: ")
inch = cm_to_inch(float(number))
print(f"Length in inches: {inch}")
cms = inch_to_cm(inch)
print(f"Length in cms: {cms}")
