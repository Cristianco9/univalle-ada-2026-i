#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 3
"""
Dividir cada número en dos mitades y usar el algoritmo de Karatsuba
para reducir el número de multiplicaciones.
"""
def karatsuba(x, y):

    # caso base
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # dividir números
    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    # tres multiplicaciones recursivas
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    # combinar resultados
    return ac * 10**(2*m) + ad_bc * 10**m + bd

num1 = 12345678
num2 = 87654321

resultado = karatsuba(num1, num2)

print("----- MULTIPLICACIÓN KARATSUBA -----")
print("Número 1:", num1)
print("Número 2:", num2)
print("Resultado:", resultado)
print("------------------------------------")