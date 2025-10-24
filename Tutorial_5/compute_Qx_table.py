import numpy as np
import pandas as pd
from scipy.stats import norm

# Define Q(x) = 1 - Φ(x)
def Q(x):
    return 1 - norm.cdf(x)

# Define the range of x values
x_values = np.arange(0, 5, 0.01)  # from 0 to 5 in steps of 0.1

# Compute Q(x) for each x
q_values = [Q(x) for x in x_values]

# Create a table using pandas
table = pd.DataFrame({
    "x": np.round(x_values, 4),
    "Q(x)": np.round(q_values, 8)
})

# Print the table
print(table.to_string(index=False))


# Compute the Q(x) in Q5
z_1   = 0.7906
q_z_1 = Q(z_1)

print(f'Q({z_1}) = {q_z_1}')
