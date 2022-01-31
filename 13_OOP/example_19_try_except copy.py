# Basic form
try:
    print(5/0)
except (ZeroDivisionError, Exception) as e:
    print(f"It is forbidden to divide with 0!")

# Block chaining
class B(Exception):
    pass

class C(Exception):
    pass

class D(Exception):
    pass

for ex in [B, C, D]:
    try:
        raise ex()
    except C:
        print("C")
    except D:
        print("D")
    except B:
        print("B")

# Else clause
try:
    name = input("Input file name: ")
    # Always read file inside try block
    with open(name) as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"File {name} not found!")
else:
    print(f"File loaded succesfully!")

# Finally clause
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Forbidden division with {b}")
    else:
        return result
    finally:
        return "This is always returned!"

print(divide(5, 0))
print(divide(5, 1))
