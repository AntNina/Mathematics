# %matplotlib inline


import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

warnings.filterwarnings('ignore')


# код, который будет переводить полярные координаты в декартовы


def polar2cart(r, phi):
    x = r*math.cos(phi)
    y = r*math.sin(phi)
    return x, y


polar2cart(2, 45)

# код, который будет рисовать график окружности в полярных координатах

phi = np.arange(0., 2., 1./180.)*np.pi

plt.polar(phi, [10]*len(phi))

plt.show()

# код, который будет рисовать график отрезка прямой линии в полярных координатах

phi = np.arange(4, 8, 2)
print(phi)
rho = np.arange(4, 8, 2)
print(rho)

plt.polar(phi, rho)

plt.show()
