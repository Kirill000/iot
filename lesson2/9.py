import matplotlib.pyplot as plt
import math
import numpy as np

x_c = [i/10 for i in range(20, 90)]
y = [i/10 for i in range(0, 60)]

def fun(x, y):
    return 0.25*math.sin(0.5*(x**2)-y)-math.exp(-((x-5)**2+(y-2)**2))

f = np.vectorize(fun)
x = np.linspace(2, 9, num=71)
y = np.linspace(0, 6, num=61)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig, ax = plt.subplots(1, 1, figsize=(6, 5))
obj = ax.imshow(Z, cmap=plt.cm.seismic)
plt.show()