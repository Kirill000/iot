from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

func = lambda y, t: y+t

f0 = float(input())
t = np.arange(0,f0,1e-3)

res = odeint(func, y0=[1], t=t)

print(round(res[len(res)-1][0], 2))