import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the CDF function
def cdf(x, y):
    # Return the joint CDF for x, y >= 0, otherwise return 0
    return (1 - np.exp(-x)) * (1 - np.exp(-y)) if x >= 0 and y >= 0 else 0

# Create a grid of x and y values
x_vals = np.linspace(0, 10, 100)  # x values from 0 to 5
y_vals = np.linspace(0, 10, 100)  # y values from 0 to 5
X, Y = np.meshgrid(x_vals, y_vals)

# Compute the CDF values over the grid
Z = np.vectorize(cdf)(X, Y)

# Plotting the CDF as a surface plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Adding labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('CDF Value')
ax.set_title('Joint CDF: $F_{X,Y}(x,y) = (1 - e^{-x})(1 - e^{-y})$')

# Show the plot
plt.show()

# Optional: Contour plot of the CDF
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, Z, 20, cmap='viridis')
plt.colorbar(contour)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour plot of Joint CDF')
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the joint PDF f(X,Y) = exp(-(x + y)) for x, y >= 0
def joint_pdf(x, y):
    return np.exp(-(x + y)) if x >= 0 and y >= 0 else 0

# Create a grid of x and y values
x_vals = np.linspace(0, 10, 100)  # x values from 0 to 5
y_vals = np.linspace(0, 10, 100)  # y values from 0 to 5
X, Y = np.meshgrid(x_vals, y_vals)

# Compute the joint PDF over the grid
Z = np.vectorize(joint_pdf)(X, Y)

# Plotting the joint PDF as a surface plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Adding labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X,Y)')
ax.set_title('Joint PDF: $f_{X,Y}(x,y) = e^{-(x+y)}$')

# Show the plot
plt.show()

# Optional: Contour plot of the joint PDF
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, Z, 20, cmap='viridis')
plt.colorbar(contour)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour plot of Joint PDF')
plt.show()
