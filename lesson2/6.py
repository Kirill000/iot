import numpy as np
def nonzero(A):
     """
     A: <np.ndarray> - матрица
     ---------------
     Returns: x, y: <int>, <int> - найденный индекс строки и столбца, соответственно
     """

     matrix = np.array(np.array(A))
     x_size = matrix.shape[0]
     y_size = matrix.shape[1]
     print(x_size)
     for x in range(0, x_size):
         for y in range(0, y_size):
             if matrix[x, y] == 1:
                 return x, y
     

A = np.zeros((100,100))
A[56,70] = 1
print(nonzero(A))