"""
Write a data visualization program.

Show several values on a graph as points.
X values are in range from 1 to 20.
Y values are squares of X.

Set scatter marker size to 50.
Set scatter color to yellow.
Set scatter edge color to red.
Also, set x value range to be from 0 to 30, and y value range to be from 0 to 900.
Graph must be saved as image_squares.png
"""
import matplotlib.pyplot as plt

x_values = range(1,20)
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=50, color='yellow', edgecolor='red')
plt.axis([0, 30, 0, 900])
plt.savefig('image_squares.png')
plt.show()
