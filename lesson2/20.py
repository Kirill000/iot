import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl
from scipy.optimize import minimize 

def gauss(z, sigma, x0, y0, a, b):
  x, y = z 
  return (x+y)**2-2*x*(y+a)-2*y*b+a+b

a, b = map(float, input().split())

from scipy.optimize import minimize 
a, b = 0, 0 
def func(t, a, b): 
  x, y = t[0], t[1] 
  return (x + y)**2 - 2 * x * (y + a) - 2 * y * b + a + b 
res = minimize(func, ((0, 0)), args=(a, b)) 
print(" ".join(str(i) for i in res.x))