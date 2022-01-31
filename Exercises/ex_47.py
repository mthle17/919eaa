"""
Write a data visualization program.

Show consecutive values on a graph as connected points.
Values are: 1, 4, 9, 16, 25, 36.

Also, add the following properties to a graph:
- line width is 5
- title is "Squares", use font size 24
- x-series caption is "Number", use font size 16
- y-series caption is "Square", use font size 12
- for all labels on axis ticks use font size 8
"""
import matplotlib.pyplot as plt

y_values = [1, 4, 9, 16, 25, 36]
plt.plot(y_values, linewidth=5)
plt.title("Squares", fontsize=24)
plt.xlabel("Number", fontsize=16)
plt.ylabel("Square", fontsize=12)
plt.tick_params(axis='both', labelsize=8)
plt.show()
