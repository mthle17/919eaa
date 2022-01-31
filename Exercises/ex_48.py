"""
Write a data visualization program.

Show several values on a graph as connected points.
X values are: 1, 3, 4, 6, 7, 9.
Y values are: 1, 5, 4, 9, 8, 13.

Also, add the following properties to a graph:
- line width is 2
- title is "Sales 2021", use font size 18
"""
import matplotlib.pyplot as plt

x_values = [1, 3, 4, 6, 7, 9]
y_values = [1, 5, 4, 9, 8, 13]
plt.plot(x_values, y_values, linewidth=5)
plt.title("Sales 2021", fontsize=24)
plt.show()
