# %matplotlib inline
from unicodedata import decimal

import numpy as np
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from math import factorial
from decimal import Decimal

k, n = 100, 200
a = np.random.randint(0, 3, n)
b = np.random.randint(0, 3, n)
c = np.random.randint(0, 3, n)
d = np.random.randint(0, 3, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
# print(a, b, c, d)
# print(x)
print(k, n, k / n)

p = k / n

def num_of_successes(n, k):
    return (factorial(n) // (factorial(k) * factorial(n - k)))


def probability_of_success(p, n, k):
    C_kn = num_of_successes(n, k)
    return C_kn * (p ** k) * (1 - p) ** (n - k)


print(probability_of_success(p, n, k))