nans = list(map(int, input().split()))
ans = 0
for nan_num in range(len(nans)-2):
    if (nans[nan_num+1]-nans[nan_num])/0.01 > ans:
        ans = (nans[nan_num+1]-nans[nan_num])/0.01

print(ans)