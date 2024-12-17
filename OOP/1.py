import math
from itertools import combinations

class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float)), \  
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_string(cls, string):
        string = string.strip('{}')
        x, y, z = map(float, string.split(','))
        return cls(x, y, z)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Умножение возможно только с числом или другим вектором")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Упражнение №1.1: Центр масс
points = [Vector.from_string("{1, 2, 3}"), Vector.from_string("{4, 5, 6}"), Vector.from_string("{7, 8, 9}")]
sum_vector = sum(points, Vector(0, 0, 0))
num_points = len(points)
center_of_mass = sum_vector * (1 / num_points)
print(center_of_mass)

# Упражнение №1.2: Площадь треугольника

def triangle_area(v1, v2, v3):
    side1 = abs(v2 - v1)
    side2 = abs(v3 - v1)
    cross_product = Vector(
        side1.y * side2.z - side1.z * side2.y,
        side1.z * side2.x - side1.x * side2.z,
        side1.x * side2.y - side1.y * side2.x
    )
    return abs(cross_product) / 2

max_area = 0
max_triangle = None
for v1, v2, v3 in combinations(points, 3):
    area = triangle_area(v1, v2, v3)
    if area > max_area:
        max_area = area
        max_triangle = (v1, v2, v3)

print(max_area)



