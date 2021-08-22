import math


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """функция умножения на число"""
        return Vec2d(self.x * other, self.y * other)

    def __len__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def int_pair(self):
        """функция для возвращения целых координат"""
        return int(self.x), int(self.y)
