"""
hash_table.py
-------------

Implementación de una Tabla Hash utilizando encadenamiento separado
(Separate Chaining) para la resolución de colisiones.

Este módulo forma parte de los algoritmos y estructuras de datos
empleados en el proyecto de clasificación de complejidad algorítmica.

La estructura permite almacenar pares clave-valor y realizar
operaciones de inserción y búsqueda en tiempo promedio constante O(1).

Arquitectura:
-------------
            Key
             │
             ▼
      Hash Function
             │
             ▼
      Bucket Index
             │
             ▼
      Linked Bucket
             │
             ▼
      [key, value]

Características:
----------------
- Inserción de elementos.
- Actualización de valores existentes.
- Búsqueda por clave.
- Resolución de colisiones mediante listas.
- Complejidad promedio O(1).

Tecnologías utilizadas:
-----------------------
- Python
- Hashing
- Separate Chaining

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""


class HashTable:
    """
    Implementación básica de una Tabla Hash.

    Utiliza una función hash para transformar una clave
    en una posición dentro de un arreglo de buckets.

    Cada bucket almacena una lista de pares [key, value]
    permitiendo manejar colisiones mediante encadenamiento.

    Attributes
    ----------
    size : int
        Tamaño total de la tabla hash.

    table : list
        Estructura principal que almacena los buckets.
    """

    def __init__(
        self,
        size=100
    ):
        """
        Inicializa la tabla hash.

        Se crea una lista de buckets vacíos donde se
        almacenarán los pares clave-valor.

        Parameters
        ----------
        size : int, optional
            Número de buckets de la tabla.

        Time Complexity
        ---------------
        O(n)

        donde n es el tamaño de la tabla.

        Space Complexity
        ----------------
        O(n)
        """

        self.size = size

        self.table = [
            []
            for _ in range(size)
        ]

    def _hash(
        self,
        key
    ):
        """
        Calcula el índice asociado a una clave.

        Utiliza la función hash nativa de Python y
        posteriormente aplica la operación módulo
        para garantizar que el índice permanezca
        dentro de los límites de la tabla.

        Parameters
        ----------
        key : Any
            Clave a transformar.

        Returns
        -------
        int
            Posición dentro de la tabla hash.

        Time Complexity
        ---------------
        O(1)

        Space Complexity
        ----------------
        O(1)
        """

        return (
            hash(key)
            % self.size
        )

    def set(
        self,
        key,
        value
    ):
        """
        Inserta o actualiza un elemento en la tabla hash.

        Si la clave ya existe, su valor es actualizado.
        Si no existe, se agrega un nuevo par clave-valor
        al bucket correspondiente.

        Parameters
        ----------
        key : Any
            Clave de almacenamiento.

        value : Any
            Valor asociado a la clave.

        Time Complexity
        ---------------
        Promedio:
            O(1)

        Peor caso:
            O(n)

        cuando todas las claves colisionan en el mismo bucket.

        Space Complexity
        ----------------
        O(1)
        """

        index = self._hash(
            key
        )

        # Buscar si la clave ya existe
        for pair in (
            self.table[index]
        ):

            if (
                pair[0]
                == key
            ):

                # Actualizar valor existente
                pair[1] = value

                return

        # Insertar nuevo elemento
        self.table[
            index
        ].append(
            [key, value]
        )

    def get(
        self,
        key
    ):
        """
        Recupera el valor asociado a una clave.

        Realiza una búsqueda dentro del bucket
        correspondiente al índice generado por
        la función hash.

        Parameters
        ----------
        key : Any
            Clave a buscar.

        Returns
        -------
        Any
            Valor asociado a la clave.

        None
            Si la clave no existe.

        Time Complexity
        ---------------
        Promedio:
            O(1)

        Peor caso:
            O(n)

        Space Complexity
        ----------------
        O(1)
        """

        index = self._hash(
            key
        )

        # Buscar la clave dentro del bucket
        for pair in (
            self.table[index]
        ):

            if (
                pair[0]
                == key
            ):

                return pair[1]

        # Clave no encontrada
        return None


if __name__ == "__main__":
    """
    Ejemplo de uso de la tabla hash.
    """

    hash_table = HashTable()

    hash_table.set(
        "Cristian",
        "Software Engineer"
    )

    hash_table.set(
        "Katherine",
        "Researcher"
    )

    print(
        hash_table.get("Cristian")
    )

    print(
        hash_table.get("Katherine")
    )

    print(
        hash_table.get("Unknown")
    )