from scipy.spatial import Delaunay
import numpy as np

def linear_interpolation(points, values, interpolation_points):
    # Преобразование в numpy array
    points = np.array(points)
    
    # Триангуляция Делоне
    tri = Delaunay(points)
    
    # Находим индексы треугольников, в которых находятся точки интерполяции
    containing_triangles = tri.find_simplex(interpolation_points)
    
    interpolated_values = []

    for i in range(len(containing_triangles)):
        triangle = tri.points[tri.simplices[containing_triangles[i]]]
        bcoords = tri.transform[containing_triangles[i], :triangle.shape[1]]
    
    # Исправление индекса в целое число
    index = tri.simplices[containing_triangles[i]][0]
    
    # Линейная интерполяция
    interpolated_value = np.dot(bcoords, values[index])
    
    interpolated_values.append(interpolated_value)
    
    return interpolated_values

# Пример использования
# points = [[0, 0], [1, 0], [0, 1]]
# values = [3, 4, 5]
# interpolation_points = [[0.5, 0.5], [0.8, 0.2]]

# result = linear_interpolation(points, values, interpolation_points)
# print(result)