#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 6
"""
Implementa el algoritmo de Strassen para multiplicación de matrices. Escribe su 
recurrencia y calcula su complejidad.
"""
# -------------------------------------------------------------------------
# Recurrencia
# T(n) =
#   θ(1)              si n = 1
#   7T(n/2) + n^2     si n > 1
# -------------------------------------------------------------------------
# Teorema Maestro
# a = 7
# b = 2
# f(n) = n^2
# -------------------------------------------------------------------------
# cálculo
# n^(log₂7) ≈ n^2.81
# -------------------------------------------------------------------------
# comparación
# f(n) = θ(n^2) < n^2.81
# caso 1
# T(n) = θ(n^log₂7)
# -------------------------------------------------------------------------
# resultado
# T(n) ≈ θ(n^2.81)
# multiplicación clásica: θ(n^3)
# -------------------------------------------------------------------------
def sumar(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def restar(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def strassen(A, B):

    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mitad = n // 2

    A11 = [row[:mitad] for row in A[:mitad]]
    A12 = [row[mitad:] for row in A[:mitad]]
    A21 = [row[:mitad] for row in A[mitad:]]
    A22 = [row[mitad:] for row in A[mitad:]]

    B11 = [row[:mitad] for row in B[:mitad]]
    B12 = [row[mitad:] for row in B[:mitad]]
    B21 = [row[:mitad] for row in B[mitad:]]
    B22 = [row[mitad:] for row in B[mitad:]]

    M1 = strassen(sumar(A11,A22), sumar(B11,B22))
    M2 = strassen(sumar(A21,A22), B11)
    M3 = strassen(A11, restar(B12,B22))
    M4 = strassen(A22, restar(B21,B11))
    M5 = strassen(sumar(A11,A12), B22)
    M6 = strassen(restar(A21,A11), sumar(B11,B12))
    M7 = strassen(restar(A12,A22), sumar(B21,B22))

    C11 = sumar(restar(sumar(M1,M4),M5),M7)
    C12 = sumar(M3,M5)
    C21 = sumar(M2,M4)
    C22 = sumar(restar(sumar(M1,M3),M2),M6)

    C = [[0]*n for _ in range(n)]

    for i in range(mitad):
        for j in range(mitad):
            C[i][j] = C11[i][j]
            C[i][j+mitad] = C12[i][j]
            C[i+mitad][j] = C21[i][j]
            C[i+mitad][j+mitad] = C22[i][j]

    return C


# prueba
A = [[1,2],
     [3,4]]

B = [[5,6],
     [7,8]]

C = strassen(A,B)

print("---- STRASSEN ----")
print("Matriz A:", A)
print("Matriz B:", B)
print("Resultado:", C)
print("------------------")