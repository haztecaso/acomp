#!/usr/bin/env python3
# Ejecutar "python3 test4.py" en la terminal en la carpeta donde se
# encuentra el fichero actividad4.py.


from random import randint as rand
from timeit import timeit

from actividad4 import base2_a_decimal


def remover_ceros(a):
    # a = lista de digitos decimales
    n = len(a)
    while n >= 1 and a[n - 1] == 0:
        n -= 1
    del a[n:]


def test_assert(n, expected):
    result = base2_a_decimal(n)
    assert expected == result, f"Error"


def test():
    global n, expected
    i = 0
    xs = [rand(0, 10**i) for i in range(100)] + [
        rand(0, 10 ** (2**i)) for i in range(15)
    ]
    args = [
        (
            list(reversed(list(map(int, list(bin(x)[2:]))))),
            list(reversed(list(map(int, list(str(x)))))),
        )
        for x in xs
    ]
    T = 0
    for i in range(len(args)):
        n, expected = args[i]
        t = timeit("test_assert(n,expected)", globals=globals(), number=1)
        T += t
        print(f"Test {i:03d}:\t{t:.6f}s\t{T:.6f}s")
        i += 1


if __name__ == "__main__":
    test()
