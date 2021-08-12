"""
Цель - написать программу (скрипт), которая будет запускаться из командной строки. 
Программа принимает в качестве аргумента строку, состоящую из цифр. Гарантируется, что 
других символов в переданном параметре нет и на вход всегда подается не пустая строка. 
Программа должна вычислить сумму цифр из которых состоит строка и вывести полученный 
результат на печать в стандартный вывод.

Тесты:
> python 1_Sum_of_digits.py 12345
15
> python 1_Sum_of_digits.py 160438521039
42
"""
import sys


def get_sum_of_digit(sequence_of_digits: str) -> str:
    sum_of_digit = 0
    for digit in sequence_of_digits:
        sum_of_digit += int(digit)
    return str(sum_of_digit)


if __name__ == "__main__":
    print(get_sum_of_digit(sys.argv[1]))
