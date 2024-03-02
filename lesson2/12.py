from scipy.integrate import odeint
import numpy as np

def func(y,t):
    return y-t

t = np.arange(0,1,2)

res = odeint(func, y0=0, t=t)

print(res)
