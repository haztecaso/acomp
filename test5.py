#!/usr/bin/env python3

from actividad5 import f

cases = [
    (12345, 10, 1),
    (1993, 10, 2),
    (10**100, 10, 100),
    (10**100, 2, 100),
    (10**100, 3, 7),
]

if __name__ == "__main__":
    """
    Tests
    """
    for (n, b, expected) in cases:
        assert (
            f(n, b) == expected
        ), f"f({n}, {b}) = {f(n,b)} pero debería valer {expected}"
    print("Tests pasados :)")
