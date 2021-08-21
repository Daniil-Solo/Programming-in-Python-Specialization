import unittest
from factorize_function import factorize


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        """
        Проверяет, что передаваемый в функцию аргумент типа float или str
        вызывает исключение TypeError. Тестовый набор входных данных:  'string',  1.5
        """
        cases = ['string', 1.5]
        for case in cases:
            with self.subTest(case=case):
                self.assertRaises(TypeError, factorize, x=case)

    def test_negative(self):
        """
        Проверяет, что передача в функцию factorize отрицательного числа
        вызывает исключение ValueError. Тестовый набор входных данных:   -1,  -10,  -100
        """
        cases = [-1, -10, -100]
        for case in cases:
            with self.subTest(case=case):
                self.assertRaises(ValueError, factorize, x=case)

    def test_zero_and_one_cases(self):
        """
        Проверяет, что при передаче в функцию целых чисел 0 и 1, возвращаются соответственно кортежи (0,) и (1,).
        Набор тестовых данных: 0 → (0, ),  1 → (1, )
        """
        cases = [0, 1]
        solutions = [(0, ), (1, )]
        for case, solution in zip(cases, solutions):
            with self.subTest(case=case):
                self.assertEqual(factorize(case), solution)

    def test_simple_numbers(self):
        """
        Проверяет, что для простых чисел возвращается кортеж, содержащий одно данное число.
        Набор тестовых данных: 3 → (3, ),  13 → (13, ),   29 → (29, )
        """
        cases = [3, 13, 29]
        solutions = [(3,), (13,), (29,)]
        for case, solution in zip(cases, solutions):
            with self.subTest(case=case):
                self.assertEqual(factorize(case), solution)

    def test_two_simple_multipliers(self):
        """
        Проверяет случаи, когда функция factorize возвращает кортеж с числом элементов равным 2.
        Набор тестовых данных: 6 → (2, 3),   26 → (2, 13),   121 --> (11, 11)
        """
        cases = [6, 26, 121]
        solutions = [(2, 3), (2, 13), (11, 11)]
        for case, solution in zip(cases, solutions):
            with self.subTest(case=case):
                self.assertEqual(factorize(case), solution)

    def test_many_multipliers(self):
        """
        проверяет случаи, когда функция factorize возвращает кортеж с числом элементов больше 2.
        Набор тестовых данных: 1001 → (7, 11, 13) ,   9699690 → (2, 3, 5, 7, 11, 13, 17, 19)
        """
        cases = [1001, 9699690]
        solutions = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for case, solution in zip(cases, solutions):
            with self.subTest(case=case):
                self.assertEqual(factorize(case), solution)


if __name__ == "__main__":
    unittest.main()
