# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

z = np.random.rand(2)

k, m = 0, 0
n = 5000
for i in range(0, n):
    x = np.random.randint(0, 2)
    if x == 1:
        k += 1
    else:
        m += 1
print(k, m)
print(f"Вероятность выпадения двух одинаковых подряд", (k / (m + k)) * (m / (m + k)))
