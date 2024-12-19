import numpy as np

r, a = map(float, input().split())
circumference = 2 * np.pi * r
circle_area = np.pi * r ** 2
area_square = a ** 2
percentage = (circle_area / area_square) * 100

print(f'Длина окружности: {circumference:.2f}. \n'
      f'Площадь круга составляет {percentage:.2f}% от площади квадрата.')
