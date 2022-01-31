"""
Create program that calculates distance between two points.
It starts with following tuples:
    p1 = (1,3)
    p2 = (4,7)

Then it calculates the distance using Pythagorean theorem:
    c = sqrt(a**2 + b**2)

*EXAMPLE*
Distance between (1, 3) and (4, 7) is 5.0
"""
import math

p1 = (1,3)
p2 = (4,7)

a = p2[0] - p1[0]
b = p2[1] - p1[1]
c = math.sqrt(a**2 + b**2)

print(f"Distance between {p1} and {p2} is {c}")
