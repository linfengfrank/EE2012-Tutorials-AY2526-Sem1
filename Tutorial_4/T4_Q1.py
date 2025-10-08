import numpy as np
import matplotlib.pyplot as plt

# Define values
x_vals = np.array([-1, 0, 1])
y_vals = np.array([-1, 0, 1])

# PMFs
p_x = np.array([1/3, 1/3, 1/3])
p_y = np.array([0.5, 0.2, 0.3])

# Joint PMF (since independent: outer product)
pmf_joint = np.outer(p_x, p_y)

# Check total probability
print("Sum of joint PMF =", pmf_joint.sum())

# Create grid for plotting
X, Y = np.meshgrid(x_vals, y_vals, indexing="ij")

# Flatten for bar3d
xpos = X.flatten()
ypos = Y.flatten()
zpos = np.zeros_like(xpos)

dx = dy = 0.3
dz = pmf_joint.flatten()

# Plot
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True)

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("P(X,Y)")
ax.set_title("Joint PMF of X and Y")

plt.show()
