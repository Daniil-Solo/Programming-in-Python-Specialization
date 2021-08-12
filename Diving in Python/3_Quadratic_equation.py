"""
Задача - написать программу, которая запускается в командной строке с параметрами,
вычисляет значения корней квадратного уравнения и выводит их на печать. На вход
программе подаются целые коэффициенты a, b и c. На печать должно выводиться два корня
квадратного уравнения (каждый с новой строки). Чтобы не усложнять задачу все
коэффициенты таковы, что в итоге дают 2 корня квадратного уравнения.

Тесты:
> python 3_Quadratic_equation.py 1 -3 -4
4
-1
> python 3_Quadratic_equation.py 13 236 -396
1
-19
"""
import math
import sys


def print_roots_quadratic_equation(a: int, b: int, c: int) -> None:
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        x = int(-b / (2 * a))
        print(str(x))
        print(str(x))
    else:
        # подразумевается только D > 0
        x1 = int((-b + math.sqrt(discriminant)) / (2 * a))
        x2 = int((-b - math.sqrt(discriminant)) / (2 * a))
        print(str(x1))
        print(str(x2))


if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    print_roots_quadratic_equation(a, b, c)
