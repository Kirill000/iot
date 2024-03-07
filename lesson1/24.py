import math


def fun(x):
    return math.sin(x)
def trapez(func, a, b, N):
    h = (b-a)/N
    return round((fun(a)+fun(b)+sum(fun(a+step*h) for step in range(1, N)))*h, 8)

a, b, c, d = map(str, input().split())
print(trapez(str(a), int(b), int(c), int(d)))