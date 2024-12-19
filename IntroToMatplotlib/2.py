import numpy as np
import matplotlib.pyplot as plt

mu = 0
sigma = 1

n_points = [10, 50, 100, 500, 1000, 10000]

fig, ax = plt.subplots(3, 2, figsize=(12, 9))

for idx, n in enumerate(n_points):
    r, c = divmod(idx, 2)
    data = np.random.normal(mu, sigma, n)
    ax[r, c].hist(data, bins=n, density=True, alpha=0.9)
    ax[r, c].set_title(f"Размер выборки: {n}")
    
    x_vals = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    ax[r, c].plot(x_vals, (1 / (sigma * np.sqrt(2 * np.pi))) * 
                  np.exp(-((x_vals - mu) ** 2) / (2 * sigma**2)))

plt.tight_layout()
plt.show()
