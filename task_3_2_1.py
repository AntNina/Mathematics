# %matplotlib inline


import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

warnings.filterwarnings('ignore')

# координаты X, Y
x = 3
y = 6

# Вычисляем длину вектора
len_vec = np.sqrt(x ** 2 + y ** 2)

# Выводим длину вектора
print('Length = ', len_vec)
