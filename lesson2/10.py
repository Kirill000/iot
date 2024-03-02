import matplotlib.pyplot as plt
import numpy as np

def func(x, y):
    return np.sin(x**2+y**2)/(x**2+y**2)

f = np.vectorize(func)
x = np.linspace(2, 9, num=71)
y = np.linspace(0, 6, num=61)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig, ax = plt.subplots(1, 1, figsize=(8, 8), subplot_kw={'projection': "3d"})
ax.plot_surface(X, Y, Z / Z.max(), cmap=plt.cm.ocean_r)
ax.view_init(30, 60)

plt.show()
