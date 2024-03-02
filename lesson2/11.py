import matplotlib.pyplot as plt
import numpy as np

R = 10

def x(R, r, phi, theta):
    return (R+r*np.cos(phi))*np.cos(theta)

def y(R, r, phi, theta):
    return (R+r*np.sin(phi))*np.sin(theta)

def z(x, y):
    return (x**2+y**2)

phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, 2*np.pi, 100)
r = np.linspace(0, R, 100)

xf = np.vectorize(x)
yf = np.vectorize(y)
zf = np.vectorize(z)

X, Y = np.meshgrid(xf(R, r, phi, theta), yf(R, r, phi, theta))
Z = zf(X, Y)

fig, ax = plt.subplots(1, 1, figsize=(8, 8), subplot_kw={'projection': "3d"})
ax.plot_surface(X, Y, Z, cmap=plt.cm.ocean_r)
ax.view_init(30, 60)

plt.show()