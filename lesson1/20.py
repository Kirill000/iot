n = 0
summ = 0
x = float(input())
while True:
    n_sum = (((-1)**n)*(x**(n+1)))/(n+1)
    # if abs(n_sum) < 10**(-6):
    #     break
    if n == 60:
        break
    summ = summ + n_sum
    n += 1
print(round(summ, 8))
