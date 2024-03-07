import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl
from scipy.optimize import minimize 

def gauss(z, sigma, x0, y0):
  x, y = z 
  return np.exp(-((x-x0)**2 + (y-y0)**2) / sigma**2) 

neg_gauss = lambda z, sigma, x0, y0: -gauss(z, sigma, x0, y0) 
x = np.linspace(-20, 20, 100) 
y = np.linspace(-20, 20, 100) 
X, Y = np.meshgrid(x, y) 
Z = gauss((X, Y), 100, 0, 0) 
fig, ax = plt.subplots(1, 1, figsize=(6, 6)) 
contours = plt.contour(X, Y, Z, 15, colors="black", linewidths=2, linestyles='-.') 
ax.clabel(contours, inline = True, fontsize=16) 
contours = plt.contourf(X, Y, Z, 200, cmap=plt.cm.hsv, alpha=0.7) 
ax.set(xlabel="Ox", ylabel="Oy") 
plt.show()

from scipy.optimize import minimize 
a, b = 0, 0 
def func(t, a, b): 
  x, y = t[0], t[1] 
  return (x + y)**2 - 2 * x * (y + a) - 2 * y * b + a + b 
res = minimize(func, ((0, 0)), args=(a, b)) 
print(" ".join(str(i) for i in res.x))

path = [(15, 10)] 
# result = minimize(neg_gauss, (15, 10), args=(100, 0, 0), callback=get_path,) 
path = np.array(path)

fig, ax = plt.subplots(1, 1, figsize=(6, 6)) 
contours = plt.contour(X, Y, Z, 15, colors="black", linewidths=2, linestyles='-.') 
ax.clabel(contours, inline = True, fontsize=16) 
contours = plt.contourf(X, Y, Z, 200, cmap=plt.cm.hsv, alpha=0.7) 
ax.scatter(path[:, 0], path[:, 1], s=400, c='yellow', marker='*', alpha=1, edgecolor='black', linewidth=2) 
ax.set(xlabel="Ox", ylabel="Oy") 
plt.show()