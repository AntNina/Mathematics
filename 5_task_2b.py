import matplotlib.pyplot as plt
import random

x = []
y = []
i = 0
while i < 10:
    x.append(random.sample(range(100), 10))
    y += x[i]
    i += 1


plt.hist(y, bins="sturges")
plt.show()
