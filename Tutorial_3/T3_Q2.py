import numpy as np
import matplotlib.pyplot as plt

# Define the values of N
n_values = np.array([1, 2, 3])

# Define alpha (from the previous solution)
alpha = 6 / 11

# Define the PMF based on the formula
pmf = alpha / n_values

# Plot the PMF
plt.stem(n_values, pmf)
plt.xlabel('n')
plt.ylabel('PN(n)')
plt.title('Probability Mass Function (PMF) of N')
plt.xticks(n_values)
plt.grid(True)
plt.show()