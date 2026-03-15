#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 4
"""
Utiliza Divide y Vencerás para calcular 𝑎^𝑏 en tiempo eficiente. Explica cómo 
este enfoque mejora el método ingenuo.
"""
# -------------------------------------------------------------------------
# Recurrencia
# T(b) =
#   θ(1)          si b = 0
#   T(b/2) + 1    si b > 0
# -------------------------------------------------------------------------
# análisis
# el exponente se divide entre 2 en cada llamada
# pasos ≈ log(b)
# -------------------------------------------------------------------------

# resultado
# T(b) = θ(log b)
# método ingenuo: θ(b)
# -------------------------------------------------------------------------

def potencia_divide_venceras(a, b):

    if b == 0:
        return 1

    mitad = potencia_divide_venceras(a, b // 2)

    if b % 2 == 0:
        return mitad * mitad
    else:
        return a * mitad * mitad

a = 3
b = 13

resultado = potencia_divide_venceras(a, b)

print("----- POTENCIACIÓN DIVIDE Y VENCERÁS -----")
print("Base:", a)
print("Exponente:", b)
print("Resultado:", resultado)
print("-----------------------------------------")