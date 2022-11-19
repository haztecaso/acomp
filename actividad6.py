#!/usr/bin/env python3

# Adrián Lattes Grassi
# 30/10/2022

# He incluido las siguientes dos funciones copiadas del módulo modular


def multiplicar_mod(a, b, N):  # 0 <= a,b < N, N >= 1
    c = a * b
    c %= N
    return c


def potencia_mod(a, k, N):  # 0 <= a < N, k >= 0, N >= 2
    if k == 0:  # caso base (k = 0)
        r = 1  # convencion: 0^0 = 1
    elif k % 2 == 0:  # k es par (k > 0)
        r = potencia_mod(a, k // 2, N)
        r = multiplicar_mod(r, r, N)
    else:  # k es impar (k > 0)
        r = potencia_mod(a, k - 1, N)
        r = multiplicar_mod(a, r, N)
    return r


def f(n: int, m: int) -> int:
    """
    Gracias al teorena de Euler-Fermat se puede hacer la siguiente reducción:
    f(n,m) = 3^(7^n) mod 10^m = 3^(7^n) mod phi(10^m)) mod 10^m

    Y por otro lado
    phi(10^m) = phi(2^m*5^m) = phi(2^m)*phi(5^m) = 2^(m-1)*(2-1)*5^(m-1)*(5-1)= 4*10^(m-1)
    """
    phi_potencia_10_m = 4 * 10 ** (m - 1)
    return potencia_mod(3, potencia_mod(7, n, phi_potencia_10_m), 10**m)
