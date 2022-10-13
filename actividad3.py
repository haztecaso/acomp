#!/usr/bin/env python3

# Adrián Lattes Grassi
# 02/10/2022


from functools import lru_cache as memoize


@memoize(maxsize=10**5)
def aux_rec(x: int, n: int, k: int, d: int):
    v = x - d**n
    if v < 0 or k == 0:
        return 0
    elif v == 0:
        return 1
    else:
        return (
            aux_rec(v, n, k - 1, d + 1)
            + aux_rec(x, n, k, d + 1)
            + aux_rec(v, n, k - 1, d)
        )


def es_suma_de_k_potencias_n(x: int, k: int, n: int) -> bool:
    return x == 0 or aux_rec(x, n, k, 1) > 0
