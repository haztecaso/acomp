#!/usr/bin/env python3
from timeit import timeit

from actividad6 import f

cases = [
    (1, 3, 187),
    (3, 4, 9627),
    (2022, 10, 4398470083),
    (
        5**100,
        100,
        3885498536840880390558163388239328561791403020448934831005492927806052986760687686813792112667714187,
    ),
]


def test(n, b, expected):
    assert f(n, b) == expected, f"f({n}, {b}) = {f(n,b)} pero debería valer {expected}"


if __name__ == "__main__":
    """
    Tests
    """
    for (n, m, expected) in cases:
        t = timeit("test(n, m, expected)", globals=globals(), number=1)
    print("Tests pasados :)")
