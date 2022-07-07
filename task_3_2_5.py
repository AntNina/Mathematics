# %matplotlib inline


import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

warnings.filterwarnings('ignore')

fig = figure(figsize=(8, 8))
ax = Axes3D(fig)
X = np.arange(-15, 15, 2)
Y = np.arange(-15, 15, 2)

X, Y = np.meshgrid(X, Y)

Z = 9 * X + 204
Z2 = 9 * X + 10
ax.plot_wireframe(X, Y, Z, linestyle='--', linewidth=1)
ax.plot_wireframe(X, Y, Z2, colors='green')

show()
