#!/usr/bin/env python3

# Adrián Lattes Grassi
# 09/09/2022

from typing import Tuple
from functools import reduce


# función para obtener el signo de un número entero
signo = lambda n: -1 if n < 0 else 1


def digitos(n: int, acc: Tuple[int, ...] = ()):
    """
    Función recursiva que devuelve una tupla con los dígitos de un número entero
    no negativo.

    acc: parámetro acumulador, se utiliza para recuperar resultados desde dentro
         hacia fuera de las llamadas recursivas.
    """
    assert n >= 0, f"El parámetro {n = } tiene que ser no negativo."
    return digitos(n // 10, (n % 10,) + acc) if n > 0 else acc


def eliminar5(n: int) -> int:
    """
    Solución al ejercicio 1.6.

    Función que elimina el dígito 5 de la representación en base decimal de un entero.
    """
    return signo(n) * reduce(
        lambda a, b: a * 10 + b, filter(lambda x: x != 5, digitos(abs(n))), 0
    )


# Solución alternativa haciendo trampas, convirtiendo tipos: int -> str -> int
eliminar5_trampa = lambda x: signo(x) * int("0" + str(abs(x)).replace("5", ""))
