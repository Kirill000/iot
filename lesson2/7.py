import numpy as np

m = np.array([3, 2, 5, 4, 1, 7])
sort_m = np.sort(m)
print(np.where(m == sort_m[0])[0][0], np.where(m == sort_m[1])[0][0], np.where(m == sort_m[2])[0][0])