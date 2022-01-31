"""
Write a data visualization program that visualizes set of 3D points.
Create points as all combinations of a 10 x 10 x 10 cube.
That refers to the following points:
(0, 0, 0)
(0, 0, 1)
(0, 0, 2)
...
(0, 0, 9)
(0, 1, 0)
(0, 1, 1)
...
(0, 9, 9)
(1, 0, 0)
(1, 0, 1)
...
(9, 9, 8)
(9, 9, 9)
"""
import matplotlib.pyplot as plt

# The way to add 3D plotting
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x_values = []
y_values = []
z_values = []
for x in range(0, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            x_values.append(x)
            y_values.append(y)
            z_values.append(z)

ax.scatter3D(x_values, y_values, z_values)
plt.show()
