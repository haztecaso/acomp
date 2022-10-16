#!/usr/bin/env python3

from typing import List

from natural import sumar, multiplicar_karatsuba


def base2_a_decimal(n: List[int]) -> List[int]:
    """
    Función que efectua el cambio de base de base binaria a decimal.
    """
    if n == []:
        return []
    r = [n[-1]]
    for d in n[-2::-1]:
        r = multiplicar_karatsuba([2], r)
        if d == 1:
            r = sumar(r, [d])
    return r
