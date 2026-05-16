import time

from algoritmos.ordenamiento_burbuja import (ordenamiento_burbuja)

from algoritmos.ordenamiento_insercion import (ordenamiento_insercion)

from algoritmos.ordenamiento_seleccion import (ordenamiento_seleccion)


class ServicioBenchmark:

    def ejecutar_ordenamiento(self, lista_personas, algoritmo, criterio):
        """
        Ejecuta el algoritmo seleccionado y mide su tiempo de ejecución.
        """

        # Crear copia de datos
        copia_personas = (lista_personas.copy())

        tiempo_inicio = (time.perf_counter())

        if algoritmo == "burbuja":

            personas_ordenadas = (ordenamiento_burbuja(copia_personas,criterio))

        elif algoritmo == "insercion":

            personas_ordenadas = (ordenamiento_insercion(copia_personas,criterio))

        elif algoritmo == "seleccion":

            personas_ordenadas = (ordenamiento_seleccion(copia_personas,criterio))

        else:
            raise ValueError("Algoritmo no válido.")

        tiempo_fin = (time.perf_counter())

        tiempo_total = (tiempo_fin- tiempo_inicio)

        return (personas_ordenadas, tiempo_total)