import numpy as np
import matplotlib.pyplot as plt

# Define the rate parameter (lambda)
lambda_param = 0.25

# Create a range of time values (x-axis)
t_values = np.linspace(0, 12, 100)

# PDF of the exponential distribution: f(t) = lambda * exp(-lambda * t)
pdf = lambda_param * np.exp(-lambda_param * t_values)

# CDF of the exponential distribution: F(t) = 1 - exp(-lambda * t)
cdf = 1 - np.exp(-lambda_param * t_values)

# Complement of the CDF: 1 - F(t) = exp(-lambda * t)
complement_cdf = np.exp(-lambda_param * t_values)

# Plotting the PDF, CDF, and complement of CDF
plt.figure(figsize=(8, 6))

# Plot the PDF
# plt.subplot(3, 1, 1)
plt.plot(t_values, pdf, label='PDF', color='blue')
plt.title(f'PDF of Exponential Distribution (lambda={lambda_param})')
plt.ylabel('PDF')
plt.xlabel('t')
plt.grid(True)

# Plot the CDF
plt.figure(figsize=(8, 6))
plt.plot(t_values, cdf, label='CDF', color='green')
plt.title(f'CDF of Exponential Distribution (lambda={lambda_param})')
plt.ylabel('CDF')
plt.xlabel('x')
plt.grid(True)

# Plot the complement of the CDF
# plt.subplot(3, 1, 3)
plt.figure(figsize=(8, 6))
plt.plot(t_values, complement_cdf, label='Complement of CDF', color='red')
plt.title(f'Complement of CDF of Exponential Distribution (lambda={lambda_param})')
plt.ylabel('1 - CDF')
plt.xlabel('x')
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()
