import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# Parameters
n = 4
p = 0.5
S = np.arange(0, n+1)

# PMF values
pmf_values = binom.pmf(S, n, p)

# Plot
plt.stem(S, pmf_values, basefmt=" ")
plt.xlabel("x")
plt.ylabel("P(X=x)")
plt.title("Binomial PMF: n=4, p=0.5")
plt.xticks(S)
plt.grid(True, linestyle="--", alpha=0.6)

# Add text labels above stems
for x, prob in zip(S, pmf_values):
    plt.text(x, prob + 0.01, f"{prob:.3f}", ha='center', fontsize=9)

plt.show()
