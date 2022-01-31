"""
Write a data visualization program that visualizes 3D graph.
Draw some connected lines on the graph.
"""
import matplotlib.pyplot as plt

# The way to add 3D plotting
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = [0, 10, 10,  0, 0,  0, 10, 10,  0,  0]
y = [0,  0, 10, 10, 0,  0,  0, 10, 10,  0]
z = [0,  0,  0,  0, 0, 10, 10, 10, 10, 10]
ax.plot(x, y, z)
plt.show()