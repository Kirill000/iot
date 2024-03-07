ans = ""
x0, y0 = map(int, input().split())
if (x0-1)**2+y0**2-4 == 0:
    ans += "yes "
else:
    ans+= "no "
if abs(x0-4)<2 and abs(y0-2)<3:
    print(ans+"yes")
else:
    print(ans+"no")






