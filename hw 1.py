#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


def y1(x):
    return np.cos(x)


def y2(x):
    return np.cos(2*x)


x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, y1(x))
plt.plot(x, y2(x))
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.show()
