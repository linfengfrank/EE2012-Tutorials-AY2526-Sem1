import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# --- Problem setup ---
n = 100
p = 0.5
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# Discrete support and PMF
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)

# Continuous x for normal curve
x_cont = np.linspace(0, n, 4000)
pdf = norm.pdf(x_cont, mu, sigma)

# --- Figure ---
plt.figure(figsize=(9, 5))

# Binomial bars
plt.bar(x, pmf, width=1.0, alpha=0.5, edgecolor='k',
        label="Binomial PMF (n=100, p=0.5)")

# Normal PDF curve
plt.plot(x_cont, pdf, linewidth=2, color="red",
         label="Normal PDF  N(50, 25)")

# Shaded regions: P(Y > 55)
# Without continuity correction: x >= 55  (green)
mask_no = (x_cont >= 55) & (x_cont <= 65)
plt.fill_between(x_cont[mask_no], 0, pdf[mask_no], alpha=0.30, color="green",
                 label="Without continuity correction (Y > 55 → x ≥ 55)")

# With continuity correction: x >= 55.5 (blue)
mask_cc = (x_cont >= 55.5) & (x_cont <= 65)
plt.fill_between(x_cont[mask_cc], 0, pdf[mask_cc], alpha=0.30, color="blue",
                 label="With continuity correction (Y > 55 → x ≥ 55.5)")

# Vertical cut lines
plt.axvline(55, linestyle='--', color='green', linewidth=1.2)
plt.axvline(55.5, linestyle='--', color='blue', linewidth=1.2)

# Zoom window and cosmetics
plt.xlim(35, 65)
plt.ylim(0, 0.085)
plt.title("Continuity Correction for P(Y > 55) when Y ~ Bin(100, 0.5)\n(Zoomed: 35 ≤ Y ≤ 65)")
plt.xlabel("Number of heads (Y)")
plt.ylabel("Probability / Density")
plt.legend(loc="upper right")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# --- (Optional) print numeric comparison ---
exact = 1 - binom.cdf(55, n, p)                # P(Y > 55) exact
approx_no = 1 - norm.cdf((55 - mu) / sigma)    # normal, no CC
approx_cc = 1 - norm.cdf((55.5 - mu) / sigma)  # normal, with CC

print(f"Exact P(Y > 55)        = {exact:.7f}")
print(f"Normal (no CC)         = {approx_no:.7f}")
print(f"Normal (with CC, 55.5) = {approx_cc:.7f}")
