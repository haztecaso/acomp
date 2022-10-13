#!/usr/bin/env python3
# Ejecutar "python3 test3.py" en la terminal en la carpeta donde se
# encuentra el fichero actividad3.py.

from typing import List, Tuple
from actividad3 import es_suma_de_k_potencias_n
from timeit import timeit

def test_args_list(l1: str, args_list: List[Tuple[int, int, int]], test_number: int):
    assert len(l1) == len(args_list), f"test-{test_number} inválido"
    E = 0
    l2 = [es_suma_de_k_potencias_n(*args) for args in args_list]
    for k in range(len(l1)):
        expected = bool(int(l1[k]))
        if expected != l2[k]:
            print(
                f"Error en test-{test_number}: es_suma_de_k_potencias_n{args_list[k]}={l2[k]} != {expected}"
            )
            E += 1
    if E == 0:
        print(f"test-{test_number} ok!")
    return E


def test1():
    # test1 (0<=x<100, k=2, n=2)
    l1 = "1110110011100100111010000110010010101100110001000110110000100100110010001110000011100100011000000110"
    args_list = [(x, 2, 2) for x in range(100)]
    return test_args_list(l1, args_list, 1)


def test2():
    # test2 (0<=x<100, k=3, n=2)
    l1 = "1111111011111110111111101111011011111110111111101111111011110110111111101111111011111110111101101111"
    args_list = [(x, 3, 2) for x in range(100)]
    return test_args_list(l1, args_list, 2)


def test3():
    # test3 (0<=x<100, k=2, n=3)
    l1 = "1110000011000000100000000001100000010000000000000000001000000000110000001000000000000000000100000000"
    args_list = [(x, 2, 3) for x in range(100)]
    return test_args_list(l1, args_list, 3)


def test4():
    # test4 (0<=x<100, k=6, n=3)
    l1 = "1111111011111100111110001111111111111111110111101001111111111011111111111111101111111010111111111111"
    args_list = [(x, 6, 3) for x in range(100)]
    return test_args_list(l1, args_list, 4)


def test5():
    # test5 (x = 8**10 + 13*(7**10) + 1, k = 15, n = 10)
    E = 0
    x = 8**10 + 13 * (7**10) + 1
    if not es_suma_de_k_potencias_n(x, 15, 10):
        print("Error en test-5")
        E += 1
    if E == 0:
        print("test-5 ok!")
    return E


def test6():
    # test6 (x = 8**10 + 13*(7**10) + 1, k = 14, n = 10)
    E = 0
    x = 8**10 + 13 * (7**10) + 1
    if es_suma_de_k_potencias_n(x, 14, 10):
        print("Error en test-6")
        E += 1
    if E == 0:
        print("test-6 ok!")
    return E


def test_time():
    t1 = timeit("test1()", globals=globals(), number=1)
    print(f"{t1 = }")
    t2 = timeit("test2()", globals=globals(), number=1)
    print(f"{t2 = }")
    t3 = timeit("test3()", globals=globals(), number=1)
    print(f"{t3 = }")
    t4 = timeit("test4()", globals=globals(), number=1)
    print(f"{t4 = }")
    t5 = timeit("test5()", globals=globals(), number=1)
    print(f"{t5 = }")
    t6 = timeit("test6()", globals=globals(), number=1)
    print(f"{t6 = }")

def test_all():
    E = 0
    E += test1()
    E += test2()
    E += test3()
    E += test4()
    E += timeit("test5()", globals=globals(), number=1)
    E += timeit("test6()", globals=globals(), number=1)
    return E

def main():
    E = test_all()
    if E == 0:
        print("aprobado!")
    else:
        print("------------")
        print(f"{E} errores!")


if __name__ == "__main__":
    test_time()
