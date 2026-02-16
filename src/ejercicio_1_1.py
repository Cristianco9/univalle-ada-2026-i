import time 

## Ejercicio 1.1 - Operación O(1)
def es_par_o_impar(n : int):
    """
    Determina si un número entero es par o impar.
    :param n: numero a evaluar
    :type n: int
    :returns: str: "par" si n es par, "impar" si n es impar
    """
    
    # COMPLEJIDAD TEMPORAL: O(1)
    # la comparación ( == 0 ) es O(1)
    # El tiempo de ejecución no depende de del tamaño de n
    # Solo se almacena el resultado booleano de la comparación (n % 2 == 0).
    # El espacio usado es constante, independiente del valor de entrada.
    if ( n % 2 == 0):
        return f'El número {n} es par'
    else:
        return f'El número {n} es impar'
    
def obtener_ultimo_digito(n : int):
    """
    Obtiene el último dígito de un número entero.
    :param n: Número entero (puede ser positivo o negativo)
    :type n: int
    :returns: int: Último dígito del número (siempre positivo)
    """
    
    # COMPLEJIDAD TEMPORAL: O(1)
    # sí n = 10
    # La operación módulo 10 (n % 10) es una operación aritmética que se realiza
    # en tiempo constante.
    # Solo se almacena un entero (el último dígito) en memoria.
    # El espacio usado es constante, independiente del valor de entrada.
    # La función abs() también es O(1) para manejar números negativos.
    
    return f'del número: {n} el último dígito es: {abs(n) % 10}'

def maximo_entre_dos(a: int, b: int):
    """
    Devuelve el mayor entre dos números sin usar la función max() incorporada.
    
    :param a: Primer número
    :type a: int
    :param b: Segundo número
    :type b: int
    :returns: int: El mayor de los dos números
    """
    
    # COMPLEJIDAD TEMPORAL: O(1)
    # Se realiza una única comparación (a > b) que es una operación primitiva.
    # El (if-else) se ejecuta en O(1).
    # El espacio utilizado no depende de los valores de a o b.
    
    # Operación O(1): comparación directa
    if(a > b):
        return f'entre {a} y {b} : {a} es mayor'
    else:
        return f'entre {a} y {b} : {b} es mayor'
    
def calcular_tiempo(m: str, fn, *args, **kwargs):
    """
    Función para calcular el tiempo de ejecución de otra función
    
    :param m: descripción de la función a ejecutar
    :type m: str
    :param fn: función a ejecutar
    :param args: parámetro 1
    :param kwargs: parámetro 2
    """
    
    # Medir tiempo de ejecución
    inicio = time.perf_counter()
    resultado = fn(*args, **kwargs) # ejecuta la función lambda
    fin = time.perf_counter()
    
    tiempo_ejecucion = (fin - inicio) * 1_000_000 
    print(f"==================================================================")
    print(f'{m}')
    print(f'Resultado: {resultado}')
    print(f'Tiempo de ejecución: {tiempo_ejecucion:.6f}')
    print(f"==================================================================")

calcular_tiempo("Determina si un número entero es par o impar.", es_par_o_impar, 9)
calcular_tiempo("Obtiene el último dígito de un número entero.", obtener_ultimo_digito, 54342679)
calcular_tiempo("Devuelve el mayor entre dos números sin usar la función max() incorporada.", maximo_entre_dos, 43, 67)
