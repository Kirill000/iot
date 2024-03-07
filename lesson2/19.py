import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl
from scipy.optimize import minimize 

dx = 0.001 
x = np.arange(-4, 4, dx)

f = lambda x: (x**2) * ((x-4)**2) * np.exp(-x**2)*(-1)
x0 = float(input())
def get_path(xc): 
  global path 
  path.append(xc)
  
x0 = 1 
path = [x0] 
result = minimize(f, x0=x0, tol=1e-2, callback=get_path) 
x1 = result.x 
print(round(x1[0], 2))