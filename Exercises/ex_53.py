"""
Write a data visualization program that visualizes matrix values as a heatmap.
Heatmap is a visualization to easily detect more dense areas.
If there are more points in the vicinity, heatmap is darker.
If there are less points in the vicinity, heatmap is darker.
Use grayscale for colors.
Note that the points are not assigned as values, but simply added to the graph.

Add the following points and values
- (3, 7)
- (4, 8)
- (5, 9)
- (6, 10)
- (15, 12)

NOTE: use nearest_neighbours() function from module heatmap_utils.
This function will calculate matrix points for feeding plt.imshow().
You will also have to feed extent parameter that nearest_neighbours() 
will return.

Function: nearest_neighbours(xs, ys, reso, max_neighbours)

Parameters:
- xs - list of x coordinates
- ys - list of y coordinates
- reso - final resolution the function returns (reso * reso), e.g. 50
- max_neighbours - just pass number of points here

Returns tuple:
- im - matrix for drawing
- extent - extent to pass to plt.imshow()
"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from heatmap_utils import nearest_neighbours

# Set points
xs = [3,4,5,6,15]
ys = [7,8,9,10,12]

num_of_points = len(xs)
im, extent = nearest_neighbours(xs, ys, 250, num_of_points)
plt.imshow(im, origin='lower', extent=extent, cmap=cm.binary)
plt.show()
