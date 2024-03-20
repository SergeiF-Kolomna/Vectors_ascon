import math                     # модуль для работы с числами

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # представление
    def __repr__(self):                     
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    # сложение векторов
    def add(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
   
    # считаем скалярное произведение
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    # считаем векторное произведение
    def cross_product(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)
    
    # считаем длину
    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    # считаем угол между векторами
    def angle_between(self, other):
        dot = self.dot_product(other)
        len_self = self.length()
        len_other = other.length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Нельзя посчитать угол с нулевым вектором.")
        cosine_theta = dot / (len_self * len_other)
        # чтобы найти угол в радианах используем arccos
        theta_radians = math.acos(max(-1, min(1, cosine_theta)))
        # Переводим радианы в градусы
        return math.degrees(theta_radians)
    
    def is_collinear(self, other):
        cross = self.cross_product(other)
        #  если векторное произведение равно нулевому вектору, то векторы коллинеарны
        return cross.x == cross.y == cross.z == 0

# Набор векторов:
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(2, 4, 6)
v3 = Vector3D(-1, -2, -3)

# Вывод результата
print("Вектор 1:", v1)
print("Вектор 2:", v2)
print("Вектор 3:", v3)
print("Сложение v1 и v2 >:", v1.add(v2))
print("Скалярное произведение:", v1.dot_product(v2))
print("Векторное произведение:", v1.cross_product(v2))
print("Длина вектора 1:", v1.length())
print("Угол между векторами 1 и 2:", v1.angle_between(v2))
print("Векторы 1 и 2 коллинеарны? >:", v1.is_collinear(v2))
print("Векторы 1 и 3 коллинеарны? >:", v1.is_collinear(v3))

