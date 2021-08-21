def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    factors = list()
    if type(x) is not int:
        raise TypeError
    if x < 0:
        raise ValueError
    elif x == 0:
        return tuple([0])
    elif x == 1:
        return tuple([1])
    else:
        while x != 1:
            number = 2
            while True:
                if x % number == 0:
                    factors.append(number)
                    break
                else:
                    number += 1
            x = x / number
        unique_factors = list(factors)
        unique_factors.sort()
        tuple_factors = tuple(unique_factors)
        return tuple_factors
