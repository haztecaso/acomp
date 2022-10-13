#!/usr/bin/env python3

# Adrián Lattes Grassi
# 07/10/2022

from typing import List


def cambio_base(n: int, b: int) -> List[int]:
    """
    Función que devuelve la representación de un entero n en base b.
    Devuelve una lista con los dígitos.
    """
    result = []
    while n > 0:
        result.append(n % b)
        n = n // b
    return result


def contar_digitos_repetidos(n: List[int]) -> int:
    """
    Dado un string con los dígitos de un número devuelve el tamaño de la
    subcadena más larga de dígitos repetidos.
    """
    maximo = 0
    contador = 1
    for i in range(1, len(n)):
        contador = contador + 1 if n[i - 1] == n[i] else 1
        if contador > maximo:
            maximo = contador
    return maximo


def f(n: int, b: int) -> int:
    """
    Función que dado un entero n >= 0 y b>=2 determina la longitud de la
    subcadena más larga de dígitos repetidos consecutivos en la expresión de n
    en base b.
    """
    assert 2 <= b <= 10, "La base debe ser un entero entre 2 y 10 (incluidos)."
    if n == 0:
        return 834  # No nos importa el 0!
    assert (
        0 < n <= 10**10000
    ), "El número de entrada debe ser positivo y menor o igual que 10^10000."
    return contar_digitos_repetidos(cambio_base(n, b))
