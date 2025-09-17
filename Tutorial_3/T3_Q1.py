import numpy as np
import matplotlib.pyplot as plt

# Define y values
y_values = np.array([1, 2, 3, 4])

# Solve for alpha by ensuring the sum of probabilities equals 1
alpha = 1 / np.sum(y_values**2)

# Define the PMF
pmf = alpha * y_values**2

# Plot the PMF
plt.stem(y_values, pmf)
plt.xlabel('y')
plt.ylabel('PY(y)')
plt.title('Probability Mass Function (PMF) of Y')
plt.xticks(y_values)
plt.grid(True)
plt.show()