"""
Write a data visualization program that visualizes matrix values.
It displays X * Y grid.
If value in grid is higher, the color is darker.
If value in grid is lower, the color is lighter.
Use grayscale for colors.

Add the following points and values
- (3, 7) => 5
- (4, 8) => 10
- (5, 9) => 15
- (6, 10) => 20
- (15, 12) => 12
"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Set width and height
width = 30
height = 20

# Create matrix with all zeroes using list comprehension
matrix = [ [ 0 for i in range(width) ] for j in range(height) ]

# Add a few items to matrix cells
matrix[3][7] = 5
matrix[4][8] = 10
matrix[5][9] = 15
matrix[6][10] = 20
matrix[15][12] = 12

# Draw
# - origin='lower' means that y is on the lower side (try removing it and see result)
# - cmap=cm.autumn_r is a grayscale colormap
#   For other colormaps, see: https://stackoverflow.com/questions/34314356/how-to-view-all-colormaps-available-in-matplotlib
plt.imshow(matrix, origin='lower', cmap=cm.binary)
plt.show()
