# algorithms/selection_sort.py


def ordenamiento_seleccion(lista_personas, criterio):
    """
    Ordena una lista de personas usando Selection Sort.
    """

    total_elementos = len(lista_personas)

    for i in range(total_elementos):

        indice_minimo = i

        for j in range(i + 1, total_elementos):

            valor_actual = getattr(lista_personas[j], criterio)

            valor_minimo = getattr(lista_personas[indice_minimo], criterio)

            if (valor_actual < valor_minimo):

                indice_minimo = j

        temporal = lista_personas[i]

        lista_personas[i] = (lista_personas[indice_minimo])

        lista_personas[indice_minimo] = temporal

    return lista_personas